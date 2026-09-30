"""Extract the approved red/cream Mancha logo from page 4 of its supplied manual."""

from pathlib import Path
from PIL import Image
import subprocess
import sys


source = Path(sys.argv[1])
destination = Path(sys.argv[2])
destination.mkdir(parents=True, exist_ok=True)
rendered = destination / "manual-page-4.png"

subprocess.run(
    ["pdftoppm", "-f", "4", "-l", "4", "-r", "220", "-png", "-singlefile", str(source), str(rendered.with_suffix(""))],
    check=True,
)

image = Image.open(rendered).convert("RGB")
scale = image.width / 960
# Page 4 contains the largest approved red logo on a white field, at the left.
region = image.crop(tuple(round(value * scale) for value in (75, 205, 337, 337)))
pixels = region.load()
points = []
for y in range(region.height):
    for x in range(region.width):
        r, g, b = pixels[x, y]
        if r > 150 and g < 100 and b < 125 and r > g * 2:
            points.append((x, y))

if not points:
    raise RuntimeError("The approved logo could not be detected on page 4")

padding = round(10 * scale)
left = max(0, min(x for x, _ in points) - padding)
top = max(0, min(y for _, y in points) - padding)
right = min(region.width, max(x for x, _ in points) + padding + 1)
bottom = min(region.height, max(y for _, y in points) + padding + 1)
region = region.crop((left, top, right, bottom))

for name, color in (("mancha-logo-red.png", (237, 1, 32)), ("mancha-logo-cream.png", (255, 241, 225))):
    output = Image.new("RGBA", region.size)
    src = region.load()
    dst = output.load()
    for y in range(region.height):
        for x in range(region.width):
            r, g, b = src[x, y]
            # White page pixels become transparent while retaining antialiasing.
            alpha = max(0, min(255, 255 - min(g, b))) if r > g * 1.15 else 0
            dst[x, y] = (*color, alpha)
    output.save(destination / name, optimize=True)

rendered.unlink()
