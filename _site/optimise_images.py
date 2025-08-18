import os
from PIL import Image

# Input/output directories
INPUT_DIR = "images_src"
OUTPUT_DIR = "images"

# Ensure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Settings
MAX_WIDTH = 1600
WEBP_QUALITY = 75
JPEG_QUALITY = 75

def optimize_image(input_path, output_path_base):
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if needed (e.g. for PNG with transparency)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Resize if larger than MAX_WIDTH
            width, height = img.size
            if width > MAX_WIDTH:
                new_height = int(height * MAX_WIDTH / width)
                img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

            # Save as WebP
            webp_path = f"{output_path_base}.webp"
            img.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)
            print(f"Optimized (WebP): {webp_path}")

            # Also save as compressed JPEG (optional fallback)
            jpg_path = f"{output_path_base}.jpg"
            img.save(jpg_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
            print(f"Optimized (JPEG): {jpg_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")


def main():
    for file_name in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, file_name)

        if not os.path.isfile(input_path):
            continue

        name, ext = os.path.splitext(file_name)
        ext = ext.lower()

        if ext not in [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"]:
            print(f"Skipping unsupported file: {file_name}")
            continue

        output_path_base = os.path.join(OUTPUT_DIR, name)
        optimize_image(input_path, output_path_base)


if __name__ == "__main__":
    main()
