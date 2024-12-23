import ctypes
import os
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(output_path, text="CODE.EUROPA.EU", image_size=(1920, 1080)):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # Use Arial font with size 80
    except:
        font = ImageFont.load_default()  # Fallback to default font if Arial is unavailable
    text_width, text_height = draw.textsize(text, font=font)

    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    draw.text(text_position, text, fill="blue", font=font)
    image.save(output_path)
    print(f"Image with text '{text}' saved to: {output_path}")


def set_wallpaper(image_path):
    if not os.path.exists(image_path):
        print("Error: The specified image file does not exist.")
        return
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    print(f"Wallpaper has been set to: {image_path}")
if __name__ == "__main__":
    OUTPUT_IMAGE_PATH = r"C:\path\to\your\open_europa_wallpaper.jpg"  # Replace with desired output path
    TEXT_TO_WRITE = "open.europa.eu"
    create_image_with_text(OUTPUT_IMAGE_PATH, TEXT_TO_WRITE)
    set_wallpaper(OUTPUT_IMAGE_PATH)













