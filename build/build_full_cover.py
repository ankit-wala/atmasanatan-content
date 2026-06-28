#!/usr/bin/env python3
"""
Build full Notion Press wraparound cover: back + spine + front.

Canvas:  3964 × 2784 px at 300 DPI  (13.212" × 9.278" — bleed included)
Layout:  42px bleed | 1800px back | 280px spine | 1800px front | 42px bleed
         + 42px bleed top and bottom

Spine:   0.934" — 420 pages cream paper.
Barcode: bottom-right of back cover — left empty (Notion Press auto-places ISBN/MRP).

Usage:
  /usr/bin/python3 build/build_full_cover.py          # full cover (back+spine+front)
  /usr/bin/python3 build/build_full_cover.py --back   # back cover only
"""

import subprocess, tempfile, os, sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# ── Paths ──────────────────────────────────────────────────────────────────────
_HERE      = os.path.dirname(os.path.abspath(__file__))
_REPO      = os.path.dirname(_HERE)
_COVER     = os.path.join(_REPO, "cover")
_ASSETS    = "/Users/ankitwala/Documents/personal_projects/atmasanatan-assets"

LOGO_PATH  = os.path.join(_ASSETS, "final logo.png")
FRONT_PATH = os.path.join(_COVER,  "front-cover-300dpi-maroon.png")
OUT_BACK   = os.path.join(_COVER,  "back-cover-300dpi.png")
OUT_FULL   = os.path.join(_COVER,  "full-cover-300dpi.png")
PANGO_VIEW = "/opt/homebrew/bin/pango-view"

# ── Dimensions ─────────────────────────────────────────────────────────────────
DPI     = 300
W, H    = 1800, 2700      # single cover trim (no bleed)
BLEED   = 42              # 0.14" each side at 300 DPI
SPINE_W = 280             # 0.934" spine — 420pp cream paper
FULL_W  = BLEED + W + SPINE_W + W + BLEED   # 3964
FULL_H  = BLEED + H + BLEED                  # 2784
SAFE    = 75              # Notion Press safe zone

# ── Colour palette ─────────────────────────────────────────────────────────────
GOLD        = "#FFD700"
GOLD_DIM    = "#C8A870"
CREAM_TEXT  = "#DDD0B0"
BULLET_TEXT = "#C8A870"

# ── Gradient — same maroon as front cover ──────────────────────────────────────
GRADIENT = [
    (0.00, [  6,  2, 12]),   # near-black
    (0.45, [ 45,  8, 16]),   # early maroon bias
    (1.00, [ 88, 12, 20]),   # rich deep maroon
]

# ──────────────────────────────────────────────────────────────────────────────
# Core helpers
# ──────────────────────────────────────────────────────────────────────────────

def make_gradient(w, h, stops):
    t   = np.linspace(0, 1, h)
    rgb = np.zeros((h, 3), dtype=np.float32)
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]; t1, c1 = stops[i + 1]
        m = (t >= t0) & (t <= t1)
        f = np.where(m, (t - t0) / (t1 - t0), 0.0)
        for ch in range(3):
            rgb[:, ch] += np.where(m, c0[ch] + f * (c1[ch] - c0[ch]), 0.0)
    canvas = np.broadcast_to(rgb[:, None, :], (h, w, 3)).copy()
    alpha  = np.full((h, w, 1), 255, dtype=np.uint8)
    rgba   = np.concatenate([canvas.astype(np.uint8), alpha], axis=2)
    return Image.fromarray(rgba, "RGBA")


def p(physical_pt):
    """Convert physical point size (at 300 DPI) to pango-view pt at --dpi=72.

    pango-view always renders at --dpi=72 here. To get correct physical size on
    the 300-DPI canvas, multiply physical pt by 300/72 so the rendered pixel
    height equals physical_pt * 300/72 ≈ physical_pt * 4.167 pixels.
    """
    return round(physical_pt * 300 / 72)


def render_text(text, pt, color=GOLD, font="Nirmala UI", weight="Regular",
                align="left", wrap_px=None):
    """Render Devanagari text via pango-view (HarfBuzz, --dpi=72).

    Pass raw pango pt (use helper p() to convert from physical pt to canvas px).
    wrap_px is in canvas pixels (converted to pango screen-pixels inside).
    """
    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w", encoding="utf-8", delete=False) as f:
        f.write(text); txt = f.name
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        out = f.name
    try:
        cmd = [
            PANGO_VIEW,
            f"--font={font} {weight} {pt}",
            f"--foreground={color}",
            "--background=transparent",
            "--dpi=72",
            "-q", f"--output={out}",
            f"--align={align}",
        ]
        if wrap_px:
            cmd += [f"--width={wrap_px}"]
        cmd.append(txt)
        subprocess.run(cmd, check=True, capture_output=True)
        img = Image.open(out).convert("RGBA")
        PAD = 20
        safe = Image.new("RGBA", (img.width + PAD * 2, img.height + PAD * 2), (0, 0, 0, 0))
        safe.paste(img, (PAD, PAD), img)
        bbox = safe.split()[3].getbbox()
        return safe.crop(bbox) if bbox else safe
    finally:
        os.unlink(txt)
        try: os.unlink(out)
        except FileNotFoundError: pass


def scale_to_w(img, w):
    s = w / img.width
    return img.resize((w, max(1, int(img.height * s))), Image.LANCZOS)


def paste_cx(canvas, img, cx, y):
    """Paste img centred at cx, return new y (bottom of pasted img)."""
    canvas.paste(img, (cx - img.width // 2, y), img)
    return y + img.height


def gold_rule(canvas, y, x0, x1, thickness=2):
    """Gold horizontal rule that fades to transparent at both ends."""
    arr  = np.array(canvas).copy()
    mid  = (x0 + x1) / 2.0
    xs   = np.arange(x0, x1)
    t    = np.abs(xs - mid) / ((mid - x0) + 1e-9)
    alph = np.clip(255 * (1 - t ** 1.4), 0, 255).astype(np.uint8)
    for row in range(y, min(y + thickness, arr.shape[0])):
        arr[row, x0:x1, 0] = 212
        arr[row, x0:x1, 1] = 175
        arr[row, x0:x1, 2] =  55
        arr[row, x0:x1, 3] = alph
    canvas.paste(Image.fromarray(arr, "RGBA"), (0, 0))


def logo_rgba(path, threshold=252):
    """Load logo, remove near-white background → RGBA."""
    img  = np.array(Image.open(path).convert("RGBA"))
    mask = (img[:, :, 0] > threshold) & \
           (img[:, :, 1] > threshold) & \
           (img[:, :, 2] > threshold)
    img[mask, 3] = 0
    return Image.fromarray(img, "RGBA")


def apply_effects(img, glow_blur=10, glow_color=(255, 160, 30), glow_alpha=185,
                  shadow_offset=(4, 5), shadow_blur=4, shadow_alpha=210):
    """Warm amber glow + drop shadow (used for spine title)."""
    w, h = img.size
    pad  = glow_blur * 2 + max(abs(shadow_offset[0]), abs(shadow_offset[1])) + 4
    out  = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    _, _, _, a = img.split()
    shad = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    shad.putalpha(a.point(lambda x: int(x * shadow_alpha / 255)))
    shad = shad.filter(ImageFilter.GaussianBlur(shadow_blur))
    out.paste(shad, (pad + shadow_offset[0], pad + shadow_offset[1]), shad)
    gl = Image.new("RGBA", (w, h), glow_color + (255,))
    gl.putalpha(a.point(lambda x: min(255, int(x * glow_alpha / 255))))
    gl = gl.filter(ImageFilter.GaussianBlur(glow_blur))
    out.paste(gl, (pad, pad), gl)
    out.paste(img, (pad, pad), img)
    bbox = out.split()[3].getbbox()
    return out.crop(bbox) if bbox else out


# ──────────────────────────────────────────────────────────────────────────────
# Back cover
# ──────────────────────────────────────────────────────────────────────────────

def build_back():
    print("  Building back cover …")
    canvas = make_gradient(W, H, GRADIENT)
    CX  = W // 2
    SX0 = SAFE       # 75
    SX1 = W - SAFE   # 1725

    # Paragraph wrap width in pixels (at --dpi=300, px = physical px on 300-DPI canvas)
    WRAP = 1400

    # ── Faint OM watermark (subtle decorative background) ────────────────────
    print("    Rendering OM watermark …")
    # 400pt at 72dpi → ~400px tall OM, placed in lower-centre at 10% opacity
    om = render_text("ॐ", 400, color="#6B0C10", font="Nirmala UI", weight="Bold")
    om_a = om.split()[3].point(lambda x: int(x * 0.10))
    om.putalpha(om_a)
    paste_cx(canvas, om, CX, H // 2 - om.height // 2 + 180)

    # Content left margin — aligned with where bullet/paragraph text starts
    CONTENT_X = SX0 + 90   # 165px — bullets, publisher block all align here

    # ── Logo (top-centre) ─────────────────────────────────────────────────────
    print("    Placing logo …")
    logo = logo_rgba(LOGO_PATH)
    LOGO_H = 170
    s = LOGO_H / logo.height
    logo = logo.resize((int(logo.width * s), LOGO_H), Image.LANCZOS)
    y = SAFE + 15   # 90
    y = paste_cx(canvas, logo, CX, y) + 55   # space after logo

    # ── Rule ─────────────────────────────────────────────────────────────────
    gold_rule(canvas, y, SX0 + 100, SX1 - 100)
    y += 65   # gap before paragraph

    # ── Description paragraph ─────────────────────────────────────────────────
    print("    Rendering paragraph …")
    para = (
        "हिंदू पंचांग का हर पर्व एक कथा से जीवित है — वह कथा जो बताती है "
        "कि यह तिथि पवित्र क्यों है, देव ने उस दिन क्या किया, "
        "और व्रत का फल क्या है।\n\n"
        "यह पुस्तक ऐसी ही १०८ कथाओं का पवित्र संकलन है — वराह के "
        "पृथ्वी-उद्धार से करवाचौथ के चंद्रदर्शन तक, शिवरात्रि की "
        "निशि-जागरण से दीपावली के लक्ष्मी-पूजन तक — प्रत्येक अध्याय में "
        "कथा, महत्त्व, विधि और अर्थ-सहित मंत्र पूर्ण रूप से हैं।"
    )
    para_img = render_text(para, p(11), color=CREAM_TEXT, font="Nirmala UI",
                           weight="Regular", align="center", wrap_px=WRAP)
    y = paste_cx(canvas, para_img, CX, y) + 60   # space before next rule

    # ── Rule ─────────────────────────────────────────────────────────────────
    gold_rule(canvas, y, SX0 + 100, SX1 - 100)
    y += 70   # gap before bullets

    # ── Bullet points ─────────────────────────────────────────────────────────
    print("    Rendering bullets …")
    bullets = [
        "❖   हिंदू वर्ष के १०८ पर्व एवं व्रत — एक ही ग्रन्थ में",
        "❖   प्रत्येक अध्याय: कथा · महत्त्व · विधि · मंत्र (अर्थ सहित)",
        "❖   सभी व्रतों की सटीक तिथियाँ — २०२६ और २०२७",
        "❖   शास्त्र-स्रोत: वाल्मीकि रामायण, श्रीमद् भागवत, स्कन्द पुराण",
        "❖   इस पुस्तक के साथ: आत्म सनातन ऐप — भजन, मंत्र, पंचांग और राशिफल",
    ]
    for bullet in bullets:
        b = render_text(bullet, p(11), color=BULLET_TEXT, font="Nirmala UI", weight="Regular")
        canvas.paste(b, (CONTENT_X, y), b)
        y += b.height + 36   # breathing room between bullets
    y += 45   # extra space after last bullet

    # ── Rule ─────────────────────────────────────────────────────────────────
    gold_rule(canvas, y, SX0 + 100, SX1 - 100, thickness=3)
    y += 90   # space before verse

    # ── Sanskrit verse + meaning ──────────────────────────────────────────────
    print("    Rendering verse …")
    verse = "व्रतेन दीक्षामाप्नोति, दीक्षयाऽऽप्नोति दक्षिणाम्।\nदक्षिणा श्रद्धामाप्नोति, श्रद्धया सत्यमाप्यते॥"
    verse_img = render_text(verse, p(10), color="#9A7850", font="Nirmala UI",
                            weight="Regular", align="center", wrap_px=1450)
    y = paste_cx(canvas, verse_img, CX, y) + 20
    attrib = render_text("— अथर्ववेद", p(9), color="#7A5838",
                         font="Nirmala UI", weight="Regular", align="center")
    y = paste_cx(canvas, attrib, CX, y) + 30
    meaning = "व्रत से दीक्षा मिलती है, दीक्षा से दक्षिणा,\nदक्षिणा से श्रद्धा जागती है, और श्रद्धा से सत्य।"
    meaning_img = render_text(meaning, p(9), color="#7A5838", font="Nirmala UI",
                              weight="Regular", align="center", wrap_px=1350)
    paste_cx(canvas, meaning_img, CX, y)

    # ── Publisher block — aligned to CONTENT_X (same left margin as bullets) ──
    # Notion Press barcode zone: approx x 1100–1725, y 2185–2625 — keep EMPTY
    print("    Placing publisher block …")
    PY = 2185
    logo_sm = logo_rgba(LOGO_PATH)
    LOGO_SM = 100
    s = LOGO_SM / logo_sm.height
    logo_sm = logo_sm.resize((int(logo_sm.width * s), LOGO_SM), Image.LANCZOS)
    canvas.paste(logo_sm, (CONTENT_X, PY), logo_sm)   # aligned with content margin

    TX = CONTENT_X + int(logo_sm.width) + 18
    pub_hi  = render_text("आत्म सनातन", p(15), color=GOLD,
                          font="Nirmala UI", weight="Bold")
    canvas.paste(pub_hi, (TX, PY + 14), pub_hi)

    web_img = render_text("app.atmasanatan.com", p(10), color=GOLD_DIM,
                          font="Nirmala UI", weight="Regular")
    canvas.paste(web_img, (TX, PY + 14 + pub_hi.height + 8), web_img)

    print(f"    Back cover done  (content to y≈{y}  |  publisher at y={PY})")
    return canvas


# ──────────────────────────────────────────────────────────────────────────────
# Spine
# ──────────────────────────────────────────────────────────────────────────────

def build_spine():
    print("  Building spine …")
    spine      = make_gradient(SPINE_W, H, GRADIENT)
    SPINE_SAFE = 28

    # Title: "१०८  व्रत कथाएँ" — NotoSerifDevanagari Black, gold, with glow
    # Render at 400pt/72dpi → rotate CCW → scale to fit spine safe-width
    title_raw = apply_effects(
        render_text("१०८  व्रत कथाएँ", 400,
                    color=GOLD, font="Noto Serif Devanagari", weight="Black")
    )
    # CCW rotation: text reads bottom-to-top on spine (standard book convention)
    title_rot = title_raw.rotate(90, expand=True)
    max_w = SPINE_W - 2 * SPINE_SAFE
    if title_rot.width > max_w:
        title_rot = scale_to_w(title_rot, max_w)

    sx = SPINE_W // 2 - title_rot.width // 2
    sy = max(SPINE_SAFE, (H - title_rot.height) // 2 - 80)
    spine.paste(title_rot, (sx, sy), title_rot)

    # Publisher: "आत्म सनातन" at bottom of spine
    pub_raw = render_text("आत्म सनातन", 120, color=GOLD_DIM,
                          font="Nirmala UI", weight="Regular")
    pub_rot = pub_raw.rotate(90, expand=True)
    if pub_rot.width > max_w:
        pub_rot = scale_to_w(pub_rot, max_w)
    px = SPINE_W // 2 - pub_rot.width // 2
    py = H - SAFE - pub_rot.height - 20
    spine.paste(pub_rot, (px, py), pub_rot)

    return spine


# ──────────────────────────────────────────────────────────────────────────────
# Full cover assembly + PDF export
# ──────────────────────────────────────────────────────────────────────────────

def build_full_cover():
    print("Building full cover …")

    full = make_gradient(FULL_W, FULL_H, GRADIENT)

    back  = build_back()
    spine = build_spine()

    if not os.path.exists(FRONT_PATH):
        print(f"\n✗  Front cover not found at {FRONT_PATH}")
        print("   Run first:  /usr/bin/python3 build/build_cover.py maroon")
        sys.exit(1)
    front = Image.open(FRONT_PATH).convert("RGBA")
    print(f"  Loaded front  ({front.width}×{front.height})")

    full.paste(back,  (BLEED,               BLEED), back)
    full.paste(spine, (BLEED + W,            BLEED), spine)
    full.paste(front, (BLEED + W + SPINE_W,  BLEED), front)

    # ── PNG ──────────────────────────────────────────────────────────────────
    full_rgb = Image.new("RGB", full.size, (0, 0, 0))
    full_rgb.paste(full, (0, 0), full)
    full_rgb.save(OUT_FULL, dpi=(DPI, DPI))
    print(f"\n✓  Full cover PNG : {OUT_FULL}")
    print(f"   {FULL_W}×{FULL_H}px  |  {FULL_W/DPI:.3f}\" × {FULL_H/DPI:.3f}\"  |  {DPI} DPI")

    # ── Back PNG separately ───────────────────────────────────────────────────
    back_rgb = Image.new("RGB", (W, H), (0, 0, 0))
    back_rgb.paste(back, (0, 0), back)
    back_rgb.save(OUT_BACK, dpi=(DPI, DPI))
    print(f"✓  Back cover PNG : {OUT_BACK}")

    # ── PDF (press-quality) ───────────────────────────────────────────────────
    pdf_path = OUT_FULL.replace(".png", ".pdf")
    try:
        import img2pdf
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(OUT_FULL, dpi=DPI))
        print(f"✓  Full cover PDF : {pdf_path}  (img2pdf — lossless)")
    except ImportError:
        full_rgb.save(pdf_path, "PDF", resolution=DPI)
        print(f"✓  Full cover PDF : {pdf_path}  (PIL fallback — install img2pdf for lossless)")


def save_back_only():
    print("Building back cover only …")
    back = build_back()
    back_rgb = Image.new("RGB", (W, H), (0, 0, 0))
    back_rgb.paste(back, (0, 0), back)
    back_rgb.save(OUT_BACK, dpi=(DPI, DPI))
    print(f"\n✓  Back cover PNG : {OUT_BACK}")


if __name__ == "__main__":
    if "--back" in sys.argv:
        save_back_only()
    else:
        build_full_cover()
