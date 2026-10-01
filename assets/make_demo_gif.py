"""Regenerate assets/demo.gif: a faithful terminal playthrough of hangman.py.

    python assets/make_demo_gif.py

Requires: pillow, matplotlib (for the bundled monospace font).
"""
import os
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager as fm

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "demo.gif")

mono = ImageFont.truetype(fm.findfont(fm.FontProperties(family="DejaVu Sans Mono")), 17)
monob = ImageFont.truetype(
    fm.findfont(fm.FontProperties(family="DejaVu Sans Mono", weight="bold")), 17)

BG, BAR = (13, 17, 23), (22, 27, 34)
FG = (201, 209, 217); GREEN = (63, 185, 80); CYAN = (57, 197, 207)
GRAY = (110, 118, 129); RED = (248, 81, 73)
W, PADX, TOP, LH = 560, 18, 46, 26
WORD = "python"


def board(guessed):
    return [((ch + " ", GREEN) if ch in guessed else ("_ ", GRAY)) for ch in WORD]


def build():
    lines = [[("$ ", GREEN), ("python hangman.py", FG)]]
    guessed, attempts, states = [], 6, []

    def snap(cursor=False):
        cp = [list(l) for l in lines]
        if cursor and cp:
            cp[-1] = cp[-1] + [("█", FG)]
        states.append(cp)

    lines.append(board(guessed)); snap(); snap(cursor=True)
    plan = [("p", "good"), ("z", "bad"), ("t", "good"), ("h", "good"),
            ("o", "good"), ("y", "good"), ("n", "win")]
    for g, kind in plan:
        lines.append([("Guess a letter: ", FG), (g, CYAN)]); snap(); snap(cursor=True)
        if kind in ("good", "win"):
            guessed.append(g)
        if kind == "bad":
            attempts -= 1
            lines.append([(f"Wrong guess! You have {attempts} attempts left.", RED)])
            lines.append(board(guessed))
        elif kind == "win":
            lines.append([("Congratulations! You guessed the word: " + WORD, GREEN)])
        else:
            lines.append(board(guessed))
        snap()
    return states


def render(lines, H):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 34], fill=BAR)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([16 + i * 22, 11, 28 + i * 22, 23], fill=c)
    d.text((W / 2 - 46, 9), "hangman", font=monob, fill=(139, 148, 158))
    y = TOP
    for line in lines:
        x = PADX
        for text, color in line:
            d.text((x, y), text, font=mono, fill=color)
            x += d.textlength(text, font=mono)
        y += LH
    return img


def main():
    states = build()
    H = TOP + LH * 18 + 14
    frames, durs = [], []
    for i, st in enumerate(states):
        frames.append(render(st, H))
        durs.append(650 if i % 2 == 1 else 350)
    frames.append(render(states[-1], H)); durs.append(1800)
    pal = frames[0].quantize(colors=64, method=Image.FASTOCTREE)
    q = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
    q[0].save(OUT, save_all=True, append_images=q[1:], duration=durs, loop=0,
              optimize=True, disposal=2)
    print("wrote", OUT, round(os.path.getsize(OUT) / 1024, 1), "KB")


if __name__ == "__main__":
    main()
