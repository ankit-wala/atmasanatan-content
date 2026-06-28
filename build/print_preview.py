#!/usr/bin/env python3
"""
Print-preview: place full-hi.pdf pages centered on A4 with a 6×9 bounding box.

Each A4 sheet has one book page centered on it with a light-grey surround and
a thin border showing the 6×9 trim area — ready to print on a home printer.

Usage:
    /usr/bin/python3 build/print_preview.py
    /usr/bin/python3 build/print_preview.py --pages 0,10,12,20
    /usr/bin/python3 build/print_preview.py --lang en

Outputs: build/output/preview-<lang>-a4.pdf
"""
import argparse
import io
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

# PDF points (1 in = 72 pt)
A4_W, A4_H = 595.28, 841.89          # A4 portrait
BK_W, BK_H = 6 * 72, 9 * 72          # 432 × 648 — 6×9 trim
TX = (A4_W - BK_W) / 2               # 81.64 — left offset to center
TY = (A4_H - BK_H) / 2               # 96.95 — bottom offset

# Default pages (0-based index into the full book PDF):
#   0  = title page
#   10 = first katha opening (Jagannath Rath Yatra)
#   12 = dense body text (mid-chapter)
#   20 = mantras section
DEFAULT_PAGES = [0, 10, 12, 20]


def make_background_reader():
    """Single-page PDF with the A4 grey surround + 6×9 white box + border."""
    from pypdf import PdfWriter, PdfReader
    from pypdf.generic import DecodedStreamObject, NameObject

    content = (
        "q\n"
        # Thin black border — the 6×9 bounding box (cut line)
        "0 0 0 RG\n"
        "0.75 w\n"
        f"{TX:.2f} {TY:.2f} {BK_W:.2f} {BK_H:.2f} re S\n"
        "Q\n"
    ).encode()

    w = PdfWriter()
    pg = w.add_blank_page(A4_W, A4_H)
    stream = DecodedStreamObject()
    stream.set_data(content)
    stream_ref = w._add_object(stream)
    pg[NameObject("/Contents")] = stream_ref

    buf = io.BytesIO()
    w.write(buf)
    buf.seek(0)
    return PdfReader(buf)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", default="hi", choices=["en", "hi"],
                        help="Language of the source book (default: hi)")
    parser.add_argument("--pages", default=None,
                        help="Comma-separated 0-based page indices (default: 0,10,12,20)")
    args = parser.parse_args()

    source_pdf = os.path.join(OUTPUT_DIR, f"full-{args.lang}.pdf")
    out_pdf    = os.path.join(OUTPUT_DIR, f"preview-{args.lang}-a4.pdf")

    page_indices = (
        [int(p.strip()) for p in args.pages.split(",")]
        if args.pages else DEFAULT_PAGES
    )

    try:
        from pypdf import PdfReader, PdfWriter, Transformation
    except ImportError:
        sys.exit("pypdf not installed.  Run: /usr/bin/pip3 install pypdf")

    if not os.path.exists(source_pdf):
        sys.exit(
            f"Source PDF not found: {source_pdf}\n"
            f"Run: /usr/bin/python3 build/to_full_book.py --lang {args.lang}"
        )

    reader = PdfReader(source_pdf)
    total  = len(reader.pages)
    print(f"Source: {source_pdf}  ({total} pages)")
    print(f"Preview pages (0-based): {page_indices}")

    bg = make_background_reader()
    writer = PdfWriter()

    for idx in page_indices:
        if idx >= total:
            print(f"  skip page {idx} — source only has {total} pages")
            continue

        src = reader.pages[idx]

        # Blank A4 canvas
        a4 = writer.add_blank_page(A4_W, A4_H)

        # 1. Grey surround + white book area + border
        a4.merge_page(bg.pages[0])

        # 2. Book page content, shifted to center
        a4.merge_transformed_page(src, Transformation().translate(TX, TY))

        print(f"  Page {idx + 1:4d} → A4 sheet {len(writer.pages)}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(out_pdf, "wb") as fh:
        writer.write(fh)
    print(f"\nSaved: {out_pdf}")


if __name__ == "__main__":
    main()
