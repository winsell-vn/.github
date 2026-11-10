#!/usr/bin/env python3
"""Render the WinSell organization avatar.

GitHub has no API for uploading an organization avatar, so the PNG is generated
here and uploaded by hand through Settings -> Profile picture. Re-run this
script after changing the mark.

    python scripts/render-avatar.py

Output: profile/assets/avatar.png (512x512, PNG).
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets" / "avatar.png"

SIZE = 512
SCALE = 4
BG = "#0b0f14"
BAR = "#121a22"
BORDER = "#1f2933"
AMBER = "#f5a623"
GREEN = "#3ddc84"

FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/consolab.ttf"),
    Path("C:/Windows/Fonts/courbd.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"),
    Path("/System/Library/Fonts/Menlo.ttc"),
]


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for candidate in FONT_CANDIDATES:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    raise SystemExit("no monospace bold font found")


def main() -> None:
    big = SIZE * SCALE
    image = Image.new("RGB", (big, big), BG)
    draw = ImageDraw.Draw(image)

    # Terminal chrome: a title bar with three traffic lights.
    bar_h = int(big * 0.13)
    draw.rectangle([0, 0, big, bar_h], fill=BAR)
    dot_r = int(big * 0.022)
    dot_y = bar_h // 2
    for index, color in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
        cx = int(big * 0.075) + index * int(big * 0.06)
        draw.ellipse(
            [cx - dot_r, dot_y - dot_r, cx + dot_r, dot_y + dot_r], fill=color
        )

    # The mark: a terminal prompt, ">_". It stays legible at 40px.
    font = load_font(int(big * 0.46))
    text = ">_"
    box = draw.textbbox((0, 0), text, font=font)
    text_w = box[2] - box[0]
    text_h = box[3] - box[1]

    # Split the glyphs so the caret and the cursor can carry different colors.
    caret_w = draw.textlength(">", font=font)
    x = (big - text_w) // 2 - box[0]
    y = (big + bar_h) // 2 - text_h // 2 - box[1]

    draw.text((x, y), ">", font=font, fill=AMBER)
    draw.text((x + caret_w, y), "_", font=font, fill=GREEN)

    # A soft amber underline anchors the mark to the terminal bar.
    underline_y = int(big * 0.80)
    draw.rectangle(
        [int(big * 0.26), underline_y, int(big * 0.74), underline_y + int(big * 0.012)],
        fill=AMBER,
    )

    # Border.
    draw.rectangle([0, 0, big - 1, big - 1], outline=BORDER, width=int(big * 0.008))

    image = image.resize((SIZE, SIZE), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} ({SIZE}x{SIZE})")


if __name__ == "__main__":
    main()
