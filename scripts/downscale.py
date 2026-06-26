import sys
from pathlib import Path

from PIL import Image

INPUT_IMAGE = Path(sys.argv[1] if len(sys.argv) > 1 else "GUI_Map.dds")
OUTPUT_SIZES = [
    # 8192,
    # 4096,
    # 2048,
    # 1024,
    512,
    256,
]


def downscale(img, size):
    return img.resize((size, size), Image.Resampling.LANCZOS)


def main():
    img = Image.open(INPUT_IMAGE).convert("RGB")

    for size in OUTPUT_SIZES:
        print(f"Generating {size}x{size}")

        resized = downscale(img, size)

        out_path = INPUT_IMAGE.with_name(
            f"{INPUT_IMAGE.stem}_{size}.{INPUT_IMAGE.suffix.lstrip('.')}"
        )
        resized.save(out_path, img.format, optimize=True)
    print("Done.")


if __name__ == "__main__":
    main()
