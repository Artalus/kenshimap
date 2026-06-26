from PIL import Image
import os

INPUT_IMAGE = "input.png"

LEVELS = [
    #(32, "5", 8192),
    #(16, "4", 4096),
    #(8,  "3", 2048),
    #(4,  "2", 1024),
    (2,  "1", 512),
    (1,  "0", 256),
]

TILE_SIZE = 256
OUT_QUALITY = 90  # WebP quality


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)


def downscale(img, size):
    return img.resize((size, size), Image.Resampling.LANCZOS)


def slice_and_save(img, grid_size, out_dir):
    ensure_folder(out_dir)

    for y in range(grid_size):
        for x in range(grid_size):
            left = x * TILE_SIZE
            top = y * TILE_SIZE
            right = left + TILE_SIZE
            bottom = top + TILE_SIZE

            tile = img.crop((left, top, right, bottom))

            filename = os.path.join(out_dir, f"{y}_{x}.webp")
            tile.save(filename, "WEBP", quality=OUT_QUALITY, method=6)


def main():
    base = Image.open(INPUT_IMAGE).convert("RGBA")

    for grid_size, folder, size in LEVELS:
        print(f"Processing level {folder}: {size} → {grid_size}x{grid_size}")

        resized = downscale(base, size)
        slice_and_save(resized, grid_size, folder)

    print("Done.")


if __name__ == "__main__":
    main()
