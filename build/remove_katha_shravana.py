#!/usr/bin/env python3
"""
remove_katha_shravana.py — remove कथा-श्रवण (read the katha) instructions from
Vidhi sections across all hi.md files.

In book layout, the katha is immediately above the Vidhi in the same chapter,
so telling readers to "hear the katha" in Vidhi is redundant.

Special cases kept intact:
  - satyanarayan-adhyaya-* : the katha shravana IS the puja; instruction is meaningful

Usage:
    /usr/bin/python3 build/remove_katha_shravana.py [--dry-run]
"""

import os
import re
import sys
import argparse

KEEP_SLUGS = {
    'satyanarayan-adhyaya-1',
    'satyanarayan-adhyaya-2',
    'satyanarayan-adhyaya-3',
    'satyanarayan-adhyaya-4',
    'satyanarayan-adhyaya-5',
}

# Matches a bullet line with label like **Label:** or **Label** (colon may be inside bold).
# Group 1 = "- **label:** " (everything up to and including closing ** plus trailing space)
# Group 2 = content after the label
BULLET_RE = re.compile(r'^(\s*-\s+\*\*[^*]+\*\*\s*)(.*?)$', re.DOTALL)

# Katha reading patterns (the clause we want to remove from content)
KATHA_READ_RE = re.compile(r'कथा[^;।\n]*(सुनें|पढ़ें|श्रवण\s*करें)')


def is_standalone_katha_bullet(line):
    """Return True if this entire bullet is only about hearing/reading the katha."""
    stripped = line.strip()
    if not stripped.startswith('-'):
        return False
    # Labels: **कथा-श्रवण:** **कथा श्रवण:** **कथा-पाठ:** **कथा:**
    # Colon is INSIDE the bold in all files: **label:**
    return bool(re.match(
        r'-\s+\*\*(कथा[-\s]?श्रवण|कथा[-\s]?पाठ|कथा):\*\*',
        stripped
    ))


def rename_compound_label(label_prefix):
    """
    Drop the कथा part from compound labels like **कथा एवं जप:** **कथा-आरती:**.
    All files use colon INSIDE bold: **label:**
    Returns the cleaned prefix.
    """
    label_prefix = re.sub(r'\*\*कथा\s*एवं\s*(जप|जाप):\*\*', r'**\1:**', label_prefix)
    label_prefix = re.sub(r'\*\*(जाप|जप)\s*व\s*कथा:\*\*', r'**\1:**', label_prefix)
    label_prefix = re.sub(r'\*\*कथा[-\s]?आरती:\*\*', '**आरती:**', label_prefix)
    label_prefix = re.sub(r'\*\*कथा[-\s]?श्रवण\s*व\s*(रात्रि\s*जागरण):\*\*', r'**\1:**', label_prefix)
    label_prefix = re.sub(r'\*\*कथा\s*व\s*(जाप|जप):\*\*', r'**\1:**', label_prefix)
    label_prefix = re.sub(r'\*\*कथा[-\s]?श्रवण\s*व\s*(आरती):\*\*', r'**\1:**', label_prefix)
    label_prefix = re.sub(r'\*\*पाठ\s*व\s*कथा:\*\*', '**पाठ:**', label_prefix)
    label_prefix = re.sub(r'\*\*जप\s*व\s*कथा:\*\*', '**जप:**', label_prefix)
    label_prefix = re.sub(r'\*\*प्रतिमा\s*व\s*कथा:\*\*', '**प्रतिमा:**', label_prefix)
    return label_prefix


def remove_katha_from_content(content):
    """
    Remove कथा-reading clauses from the content portion of a bullet.
    Content is everything after the label colon.
    Returns (new_content, changed).
    """
    if not KATHA_READ_RE.search(content):
        return content, False

    original = content

    # Remove clause: "[text] कथा [X] सुनें/पढ़ें [Y];" (clause followed by semicolon)
    content = re.sub(r'[^;।]*?कथा[^;।]*(सुनें|पढ़ें|श्रवण\s*करें)[^;।]*;\s*', '', content)
    # Remove clause: "; [text] कथा [X] सुनें/पढ़ें [Y]" (semicolon before clause)
    content = re.sub(r';\s*[^;।]*?कथा[^;।]*(सुनें|पढ़ें|श्रवण\s*करें)[^;।]*', '', content)
    # Remove " और कथा सुनें" type patterns
    content = re.sub(r'\s*(और|तथा)\s*[^;।]*?कथा[^;।]*(सुनें|पढ़ें)[^;।]*', '', content)
    # Remove remaining katha clause before sentence-end punctuation
    content = re.sub(r'[^;।]*?कथा[^;।]*(सुनें|पढ़ें|श्रवण\s*करें)[^;।]*।', '।', content)

    # Clean up artefacts
    content = re.sub(r';\s*;', ';', content)       # doubled semicolons
    content = re.sub(r';\s*।', '।', content)        # semicolon before danda
    content = re.sub(r'^\s*[;।,]\s*', '', content)  # leading punctuation
    content = content.strip()

    return content, (content != original)


def process_vidhi(vidhi_text):
    """Remove katha-shravana instructions from Vidhi section text."""
    lines = vidhi_text.split('\n')
    result = []
    changed = False

    for line in lines:
        # Case 1: entire bullet is about katha → remove
        if is_standalone_katha_bullet(line):
            changed = True
            continue

        # Case 2: mixed bullet or embedded katha mention
        m = BULLET_RE.match(line)
        if m and KATHA_READ_RE.search(line):
            prefix = rename_compound_label(m.group(1))
            content = m.group(2)
            new_content, c = remove_katha_from_content(content)
            if c:
                changed = True
                if new_content:
                    result.append(prefix + new_content)
                # else: nothing left → drop the line
                continue
            else:
                # Rename label only if it changed
                if prefix != m.group(1):
                    changed = True
                    result.append(prefix + content)
                    continue

        result.append(line)

    return '\n'.join(result), changed


def process_file(path):
    """Process one hi.md file. Returns (new_content, changed)."""
    text = open(path, encoding='utf-8').read()

    pattern = re.compile(r'(## Vidhi\n)(.*?)(?=\n## |\Z)', re.DOTALL)
    m = pattern.search(text)
    if not m:
        return text, False

    header = m.group(1)
    vidhi_body = m.group(2)
    new_body, changed = process_vidhi(vidhi_body)

    if not changed:
        return text, False

    new_text = text[:m.start()] + header + new_body + text[m.end():]
    return new_text, True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    festivals_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'kathas', 'festivals'
    )
    modified = []
    skipped = []

    for slug in sorted(os.listdir(festivals_dir)):
        if slug.startswith('_'):
            continue
        if slug in KEEP_SLUGS:
            skipped.append(slug)
            continue
        hi_path = os.path.join(festivals_dir, slug, 'hi.md')
        if not os.path.exists(hi_path):
            continue
        new_content, changed = process_file(hi_path)
        if changed:
            modified.append(slug)
            if not args.dry_run:
                open(hi_path, 'w', encoding='utf-8').write(new_content)
                print(f'  ✓ {slug}')
            else:
                print(f'  [dry-run] {slug}')

    print(f'\nDone: {len(modified)} modified, {len(skipped)} skipped (satyanarayan).')
    if args.dry_run:
        print('Re-run without --dry-run to apply.')


if __name__ == '__main__':
    main()
