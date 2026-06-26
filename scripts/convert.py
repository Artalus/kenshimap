from pathlib import Path
import sys

from PIL import Image

INPUT_FILE = Path(sys.argv[1] if len(sys.argv) > 1 else "GUI_Map.dds")
OUTPUT_FILE = Path(sys.argv[2] if len(sys.argv) > 2 else INPUT_FILE.with_suffix(".png"))
FORMAT = sys.argv[3] if len(sys.argv) > 3 else OUTPUT_FILE.suffix.lstrip(".").upper()


def main():
    print(f"{INPUT_FILE} -> {OUTPUT_FILE}")

    img = Image.open(INPUT_FILE)

    # Some DDS files load with mipmaps; ensure base level
    try:
        img.seek(0)
    except Exception:
        pass

    img = img.convert("RGB")
    img.save(OUTPUT_FILE, FORMAT)

    print(f"Saved: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
