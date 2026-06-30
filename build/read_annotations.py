#!/usr/bin/env python3
"""
read_annotations.py — extract PDF annotations and map them to katha slugs.

The merged PDF (full-hi.pdf) = front-matter PDF + chapters PDF.
Named destinations (slug anchors) live only in the chapters PDF, so we
compute the front-matter page offset and adjust accordingly.

Boundary handling: when a chapter starts mid-page (continuous flow, no forced
page breaks), annotations above the chapter heading stay with the previous katha.
This is resolved by comparing annotation y-coordinates against anchor y-coordinates
on the same page. Falls back to the previous katha if coordinates are unavailable.

NOTE: This script reads your note text (/Contents). It does NOT extract the
highlighted text itself — that requires coordinate-based text extraction (pypdf
does not support this directly). Write your note to describe the change needed.

Usage:
    /usr/bin/python3 build/read_annotations.py --pdf build/output/full-hi.pdf
    /usr/bin/python3 build/read_annotations.py --pdf build/output/full-en.pdf --lang en
"""

import sys
import os
import argparse


def get_page_count(pdf_path):
    from pypdf import PdfReader
    return len(PdfReader(pdf_path).pages)


def _try_get_dest_y(dest):
    """Try to extract the y-coordinate from a pypdf Destination object.
    Returns float (points from page bottom) or None if unavailable."""
    for approach in [
        lambda d: float(d.top),
        lambda d: float(d["/Top"]),
        lambda d: float(d.get("/Top")),
    ]:
        try:
            val = approach(dest)
            if val is not None:
                return val
        except Exception:
            pass
    return None


def extract_anchor_positions(pdf_path):
    """Return {slug: {'page': int, 'y': float|None}} from named destinations.
    y is points from the bottom of the page (higher = further up the page)."""
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)

    ref_to_num = {}
    for i, page in enumerate(reader.pages):
        ref = getattr(page, "indirect_reference", None)
        if ref is not None:
            ref_to_num[ref] = i + 1

    result = {}
    for name, dest in (reader.named_destinations or {}).items():
        try:
            pg = dest.page
            ref = getattr(pg, "indirect_reference", None)
            if ref is not None and ref in ref_to_num:
                result[name] = {
                    "page": ref_to_num[ref],
                    "y": _try_get_dest_y(dest),
                }
        except Exception:
            pass
    return result


def extract_annotations(pdf_path):
    """Return list of {page, subtype, text, y} for all text-bearing annotations.
    y is the mid-point of the annotation rect, in points from page bottom."""
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    results = []
    for i, page in enumerate(reader.pages):
        annots = page.get("/Annots")
        if not annots:
            continue
        for annot_ref in annots:
            try:
                obj = annot_ref.get_object()
                subtype = str(obj.get("/Subtype", "")).lstrip("/")
                content = obj.get("/Contents", "")
                if hasattr(content, "get_object"):
                    content = content.get_object()
                content = str(content).strip() if content else ""
                if not content:
                    continue

                # Mid-y from /Rect [x1, y1, x2, y2] (PDF coords: y increases upward)
                y = None
                rect = obj.get("/Rect")
                if rect:
                    try:
                        y = (float(rect[1]) + float(rect[3])) / 2
                    except Exception:
                        pass

                results.append({
                    "page": i + 1,
                    "subtype": subtype,
                    "text": content,
                    "y": y,
                })
            except Exception:
                pass
    return results


def find_slug_for_annotation(sorted_triples, chapter_page, annotation_y):
    """Map an annotation to a katha slug using page number and y-coordinate.

    sorted_triples: [(chapter_page, slug, anchor_y), ...] sorted by chapter_page.

    For annotations on a boundary page (where a new chapter begins mid-page):
      - If annotation_y > anchor_y: annotation is ABOVE the heading → previous katha
      - If annotation_y <= anchor_y: annotation is BELOW the heading → new katha
      - If either y is None: default to previous katha (trailing annotation is the
        common case when chapters flow continuously without forced page breaks)
    """
    result = None
    for cp, slug, anchor_y in sorted_triples:
        if cp < chapter_page:
            result = slug
        elif cp == chapter_page:
            if annotation_y is not None and anchor_y is not None:
                if annotation_y <= anchor_y:
                    result = slug   # annotation is at or below the heading
                # else: above the heading → stays with previous slug
            # y unavailable → stay with previous slug (safer default)
        else:
            break
    return result


def load_known_slugs(repo_root):
    """Return the set of valid katha slugs from the festivals directory."""
    festivals_dir = os.path.join(repo_root, "kathas", "festivals")
    if not os.path.isdir(festivals_dir):
        return set()
    return {
        name for name in os.listdir(festivals_dir)
        if os.path.isdir(os.path.join(festivals_dir, name)) and not name.startswith("_")
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract PDF annotations and map them to katha source files."
    )
    parser.add_argument("--pdf", required=True, help="Path to the annotated merged PDF")
    parser.add_argument("--lang", default="hi", choices=["en", "hi", "mr", "gu"])
    args = parser.parse_args()

    pdf_path = os.path.abspath(args.pdf)
    lang = args.lang
    output_dir = os.path.dirname(pdf_path)
    chapters_pdf = os.path.join(output_dir, f"full-{lang}-chapters.pdf")
    repo_root = os.path.dirname(os.path.dirname(output_dir))  # build/output/ → repo root

    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(chapters_pdf):
        print(f"Error: Chapters PDF not found: {chapters_pdf}", file=sys.stderr)
        print("Run to_full_book.py first to generate it.", file=sys.stderr)
        sys.exit(1)

    total_pages = get_page_count(pdf_path)
    chapters_pages = get_page_count(chapters_pdf)
    front_pages = total_pages - chapters_pages
    print(f"PDF: {total_pages} total pages  |  front matter: {front_pages}  |  chapters: {chapters_pages}")

    known_slugs = load_known_slugs(repo_root)

    anchor_positions = extract_anchor_positions(chapters_pdf)
    slug_triples = sorted(
        [
            (info["page"], name, info["y"])
            for name, info in anchor_positions.items()
            if name in known_slugs
        ],
        # Sort by page; on same page, put higher y-values first (further up = earlier in flow)
        key=lambda x: (x[0], -(x[2] or 0)),
    )

    y_resolved = sum(1 for _, _, y in slug_triples if y is not None)
    print(f"Resolved {len(slug_triples)} katha anchors ({y_resolved} with y-coordinates)")

    annotations = extract_annotations(pdf_path)
    if not annotations:
        print("\nNo annotations found in the PDF.")
        print("Make sure you saved the PDF after adding notes in Preview.")
        return

    print(f"Found {len(annotations)} annotation(s)\n")
    print("=" * 70)

    grouped = {}
    unresolved = []
    for ann in annotations:
        chapter_page = ann["page"] - front_pages
        if chapter_page <= 0:
            unresolved.append(ann)
            continue
        slug = find_slug_for_annotation(slug_triples, chapter_page, ann["y"])
        if slug:
            grouped.setdefault(slug, []).append(ann)
        else:
            unresolved.append(ann)

    for slug, anns in grouped.items():
        print(f"\n### {slug}")
        print(f"    kathas/festivals/{slug}/hi.md")
        for ann in anns:
            print(f"    [p.{ann['page']}]  {ann['text']}")

    if unresolved:
        print("\n### (unresolved — front matter or before first chapter)")
        for ann in unresolved:
            print(f"    [p.{ann['page']}]  {ann['text']}")

    print("\n" + "=" * 70)
    print(f"\nTotal: {len(annotations)} annotation(s) across {len(grouped)} katha(s)")


if __name__ == "__main__":
    main()
