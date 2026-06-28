#!/usr/bin/env python3
"""
Compose front cover — Notion Press 6×9 layout at 300 DPI.

Layout (all coords in pixels at 300 DPI):
  Canvas      : 1800 × 2700  (6" × 9" trim, no bleed)
  Safe zone   : 80px from L/R/top (was 75, nudged in 5px per user request)
  Scene image : 1640 × 2186  (3:4, fills safe-zone L/R)  at (80, 80)
  Frame       : 1700 × 2274  (3:4, slightly taller −16px)  at (50, 40)
  Text block  : TARGET_W 400px, starts at y≈2329
"""

import subprocess, tempfile, os
from PIL import Image
import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
SCENE_PATH  = "/Users/ankitwala/Downloads/Very_similar_to_the_reference_202606281748.jpeg"
FRAME_PATH  = "/Users/ankitwala/Documents/personal_projects/atmasanatan-content/cover/frame.png"
OUT_PATH    = "/Users/ankitwala/Documents/personal_projects/atmasanatan-content/cover/front-cover-300dpi.png"
PANGO_VIEW  = "/opt/homebrew/bin/pango-view"

DPI  = 300
W, H = 1800, 2700

GOLD     = "#D4AF37"
GOLD_DIM = "#9B7226"

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
        bbox = img.split()[3].getbbox()
        return img.crop(bbox) if bbox else img
    finally:
        os.unlink(txt); os.unlink(out)

def scale_to_w(img, target_w):
    s = target_w / img.width
    return img.resize((target_w, max(1, int(img.height * s))), Image.LANCZOS)

def paste_centered(canvas, img, cx, y):
    x = cx - img.width // 2
    canvas.paste(img, (x, y), img)
    return y + img.height

# ── 1. Background — Sacred Twilight gradient ──────────────────────────────────
print("Building gradient …")
stops = [
    (0.00, [  8,  2, 32]),
    (0.35, [ 32,  8, 64]),
    (0.55, [ 58, 10, 80]),
    (0.80, [128, 10, 32]),
    (1.00, [192, 32, 16]),
]
t_arr  = np.linspace(0, 1, H)
rgb_1d = np.zeros((H, 3), dtype=np.float32)
for i in range(len(stops) - 1):
    t0, c0 = stops[i];  t1, c1 = stops[i + 1]
    mask = (t_arr >= t0) & (t_arr <= t1)
    f    = np.where(mask, (t_arr - t0) / (t1 - t0), 0.0)
    for ch in range(3):
        rgb_1d[:, ch] += np.where(mask, c0[ch] + f * (c1[ch] - c0[ch]), 0.0)
rgb_2d = np.broadcast_to(rgb_1d[:, None, :], (H, W, 3)).copy()
canvas = Image.fromarray(rgb_2d.astype(np.uint8))

# ── 2. Scene image — 2.5% smaller, centered horizontally, top fixed at SY=90 ─
print("Compositing scene …")
SCALE = 0.975
SY  = 90
SW  = round((W - 90 * 2) * SCALE)        # 1580px
SH  = round(2128 * SCALE)                 # 2075px  (preserves prior aspect ratio)
SX  = (W - SW) // 2                       # 110px — centered

scene_raw = Image.open(SCENE_PATH).convert("RGBA").resize((SW, SH + 52), Image.LANCZOS)
scene = scene_raw.crop((0, 32, SW, SH + 32))  # crop 32px from top, 20px from bottom
canvas.paste(scene, (SX, SY), scene)

# ── 3. Frame — same 2.5% scale, centered, top 35px above scene ───────────────
print("Compositing frame …")
FW = round(1650 * SCALE)                  # 1609px
FX = (W - FW) // 2                        # 95px — centered
FY = SY - 35                              # 55px
FH = (SY + SH) - FY                       # flush with scene bottom → 2110px

frame = Image.open(FRAME_PATH).convert("RGBA").resize((FW, FH), Image.LANCZOS)
canvas.paste(frame, (FX, FY), frame)

# ── 5. Text block — below frame ───────────────────────────────────────────────
# Measured at 200pt/72dpi: "१०८" 297×145  |  "व्रत कथाएँ" 763×221  |  "आत्म सनातन" 1100×132
# Frame bottom = 50+2215=2265  →  text top ≈2280  →  budget=420px
# At TARGET_W=450: h108≈220, hvk≈131, hpub≈35, gaps≈21  → total≈407px ✓
print("Rendering text …")

TARGET_W = 450
PUB_W    = 290

t108 = scale_to_w(render_text("१०८",           200),                            TARGET_W)
tvk  = scale_to_w(render_text("व्रत कथाएँ",    200),                            TARGET_W)
tpub = scale_to_w(render_text("आत्म   सनातन", 200, color=GOLD_DIM, weight="Bold"), PUB_W)

FRAME_BOTTOM  = FY + FH
SAFE_BOTTOM   = H - 75          # 2625px — 75px safe zone at bottom
TEXT_PADDING  = 15              # gap between frame bottom and title

GAP_1, GAP_2 = 5, 16
TEXT_TOP     = FRAME_BOTTOM + TEXT_PADDING   # position relative to frame, not bottom

CX = W // 2
y  = TEXT_TOP
y  = paste_centered(canvas, t108, CX, y)
y += GAP_1
y  = paste_centered(canvas, tvk,  CX, y)
y += GAP_2
paste_centered(canvas, tpub, CX, y)

print(f"  Frame bottom : {FRAME_BOTTOM}px")
print(f"  Text top     : {TEXT_TOP}px")
print(f"  Text bottom  : {SAFE_BOTTOM}px  (75px from canvas edge)")
print(f"  Canvas height: {H}px")

# ── 6. Save ───────────────────────────────────────────────────────────────────
print("Saving …")
canvas.save(OUT_PATH, dpi=(DPI, DPI))
print(f"\n✓  {OUT_PATH}")
print(f"   {W}×{H} px  |  {DPI} DPI  |  {W/DPI:.2f}\" × {H/DPI:.2f}\"")
