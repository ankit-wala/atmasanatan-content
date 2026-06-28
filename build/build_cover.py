#!/usr/bin/env python3
"""
Compose front cover — Notion Press 6×9 layout at 300 DPI.

Layout (all coords in pixels at 300 DPI):
  Canvas      : 1800 × 2700  (6" × 9" trim, no bleed)
  Safe zone   : 75px from all edges (Notion Press requirement)
  Scene image : SW=1580px, SH=1895px, top at SY=90
  Frame       : FW=1609px, FH=1935px, top at FY=55 (frame bottom flush with scene bottom)
  Text block  : dynamically sized to fill frame-bottom → 75px safe zone at bottom
"""

import subprocess, tempfile, os
from PIL import Image, ImageFilter
import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
SCENE_PATH  = "/Users/ankitwala/Downloads/Very_similar_to_the_reference_202606281748.jpeg"
FRAME_PATH  = "/Users/ankitwala/Documents/personal_projects/atmasanatan-content/cover/frame.png"
OUT_PATH    = "/Users/ankitwala/Documents/personal_projects/atmasanatan-content/cover/front-cover-300dpi.png"
PANGO_VIEW  = "/opt/homebrew/bin/pango-view"

DPI  = 300
W, H = 1800, 2700

GOLD     = "#FFD700"   # bright gold (matches frame)
GOLD_DIM = "#C8960C"   # warmer, less dull for publisher line

# ── Pango text renderer (HarfBuzz shaping → correct Devanagari conjuncts) ─────
def render_text(text, pt, color=GOLD, weight="Black"):
    with tempfile.NamedTemporaryFile(suffix='.txt', mode='w', encoding='utf-8', delete=False) as f:
        f.write(text); txt = f.name
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        out = f.name
    try:
        subprocess.run([
            PANGO_VIEW,
            f"--font=Noto Serif Devanagari {weight} {pt}",
            f"--foreground={color}",
            "--background=transparent",
            "--dpi=72",
            "-q", f"--output={out}", txt,
        ], check=True, capture_output=True)
        img = Image.open(out).convert("RGBA")
        # Safety pad before bbox crop — prevents diacritics (chandrabindu, matras)
        # at the pango output boundary from being accidentally clipped.
        PAD = 16
        safe = Image.new("RGBA", (img.width + PAD * 2, img.height + PAD * 2), (0, 0, 0, 0))
        safe.paste(img, (PAD, PAD), img)
        bbox = safe.split()[3].getbbox()
        return safe.crop(bbox) if bbox else safe
    finally:
        os.unlink(txt); os.unlink(out)

def scale_to_w(img, target_w):
    s = target_w / img.width
    return img.resize((target_w, max(1, int(img.height * s))), Image.LANCZOS)

def paste_centered(canvas, img, cx, y):
    x = cx - img.width // 2
    canvas.paste(img, (x, y), img)
    return y + img.height

def apply_effects(img, glow_blur=10, glow_color=(255, 160, 30), glow_alpha=185,
                  shadow_offset=(4, 5), shadow_blur=4, shadow_alpha=210):
    """Warm amber glow + deep drop shadow behind rendered text."""
    w, h = img.size
    pad = glow_blur * 2 + max(abs(shadow_offset[0]), abs(shadow_offset[1])) + 4
    out = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    _, _, _, a = img.split()

    # Deep drop shadow
    shad = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    shad.putalpha(a.point(lambda x: int(x * shadow_alpha / 255)))
    shad = shad.filter(ImageFilter.GaussianBlur(shadow_blur))
    out.paste(shad, (pad + shadow_offset[0], pad + shadow_offset[1]), shad)

    # Warm amber glow
    gl = Image.new("RGBA", (w, h), glow_color + (255,))
    gl.putalpha(a.point(lambda x: min(255, int(x * glow_alpha / 255))))
    gl = gl.filter(ImageFilter.GaussianBlur(glow_blur))
    out.paste(gl, (pad, pad), gl)

    # Sharp bright text on top
    out.paste(img, (pad, pad), img)

    bbox = out.split()[3].getbbox()
    return out.crop(bbox) if bbox else out

def build_cover(gradient_stops, out_path):
    # ── 1. Background gradient ────────────────────────────────────────────────
    print("Building gradient …")
    t_arr  = np.linspace(0, 1, H)
    rgb_1d = np.zeros((H, 3), dtype=np.float32)
    for i in range(len(gradient_stops) - 1):
        t0, c0 = gradient_stops[i];  t1, c1 = gradient_stops[i + 1]
        mask = (t_arr >= t0) & (t_arr <= t1)
        f    = np.where(mask, (t_arr - t0) / (t1 - t0), 0.0)
        for ch in range(3):
            rgb_1d[:, ch] += np.where(mask, c0[ch] + f * (c1[ch] - c0[ch]), 0.0)
    rgb_2d = np.broadcast_to(rgb_1d[:, None, :], (H, W, 3)).copy()
    canvas = Image.fromarray(rgb_2d.astype(np.uint8))

    # ── 2. Scene image ────────────────────────────────────────────────────────
    print("Compositing scene …")
    SCALE = 0.975
    SY  = 90
    SW  = round((W - 90 * 2) * SCALE)        # 1580px
    SH  = 1895
    SX  = (W - SW) // 2                       # 110px — centered

    scene_raw = Image.open(SCENE_PATH).convert("RGBA").resize((SW, SH + 52), Image.LANCZOS)
    scene = scene_raw.crop((0, 32, SW, SH + 32))  # 32px from top, 20px from bottom
    canvas.paste(scene, (SX, SY), scene)

    # ── 3. Frame — clean resize only, never cropped ───────────────────────────
    print("Compositing frame …")
    FW = round(1650 * SCALE)                  # 1609px
    FX = (W - FW) // 2                        # 95px — centered
    FY = SY - 35                              # 55px
    FH = (SY + SH) - FY                       # flush with scene bottom

    frame = Image.open(FRAME_PATH).convert("RGBA").resize((FW, FH), Image.LANCZOS)
    canvas.paste(frame, (FX, FY), frame)

    # ── 4. Text block — dynamically sized to fill frame-bottom → safe zone ───
    print("Rendering text …")
    FRAME_BOTTOM = FY + FH
    SAFE_BOTTOM  = H - 75            # Notion Press 75px safe zone
    TEXT_PADDING = 15
    GAP_1        = 10
    TEXT_TOP     = FRAME_BOTTOM + TEXT_PADDING
    AVAILABLE_H  = SAFE_BOTTOM - TEXT_TOP

    t108_raw = apply_effects(render_text("१०८",         400))
    tvk_raw  = apply_effects(render_text("व्रत कथाएँ",  400))

    r_total  = (t108_raw.height / t108_raw.width) + (tvk_raw.height / tvk_raw.width)
    TARGET_W = int((AVAILABLE_H - GAP_1) / r_total)
    MAX_W    = W - 2 * 75
    TARGET_W = min(TARGET_W, MAX_W)

    t108 = scale_to_w(t108_raw, TARGET_W)
    tvk  = scale_to_w(tvk_raw,  TARGET_W)

    CX = W // 2
    y  = TEXT_TOP
    y  = paste_centered(canvas, t108, CX, y)
    y += GAP_1
    paste_centered(canvas, tvk, CX, y)

    print(f"  Frame bottom : {FRAME_BOTTOM}px  |  Text top: {TEXT_TOP}px  |  TARGET_W: {TARGET_W}px")

    # ── 5. Save ───────────────────────────────────────────────────────────────
    print("Saving …")
    canvas.save(out_path, dpi=(DPI, DPI))
    print(f"✓  {out_path}")


# ── Gradient presets ──────────────────────────────────────────────────────────

# Variant A — Sacred Twilight (violet-top → crimson-bottom)
GRADIENT_TWILIGHT = [
    (0.00, [  8,  2, 32]),
    (0.35, [ 32,  8, 64]),
    (0.55, [ 58, 10, 80]),
    (0.80, [128, 10, 32]),
    (1.00, [192, 32, 16]),
]

# Variant B — Deep Maroon (near-black indigo → dark burgundy)
# Inspired by reference: very dark, rich bottom like a sacred manuscript cover
GRADIENT_MAROON = [
    (0.00, [  4,  1, 18]),
    (0.35, [ 18,  5, 48]),
    (0.55, [ 35,  6, 58]),
    (0.80, [ 72,  8, 20]),
    (1.00, [ 48,  5, 12]),
]

if __name__ == "__main__":
    import sys
    variant = sys.argv[1] if len(sys.argv) > 1 else "twilight"
    if variant == "maroon":
        stops = GRADIENT_MAROON
        out   = OUT_PATH.replace(".png", "-maroon.png")
    else:
        stops = GRADIENT_TWILIGHT
        out   = OUT_PATH
    build_cover(stops, out)
