from PIL import Image, ImageFont, ImageDraw
import os, sys


def add_user_text(photo_name: str, user_text: str, user_id: int, user_name: str = "") -> None:
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    elif __file__:
        path = os.path.dirname(__file__)
    path = "\\".join(path.split('\\')[:-1])
    with Image.open(f"{path}\\data\\img\\{photo_name}") as image:
        draw = ImageDraw.Draw(image)
        font_size = 45
        text_font = ImageFont.truetype("arial.ttf", size=font_size)
        draw.text(xy=(20, 120),
                  text=user_text,
                  font=text_font,
                  fill="black")
        if user_name:
            draw.text(xy=(300, 30),
                      text=f"@{user_name}",
                      font=text_font,
                      fill="blue")
        try:
            os.mkdir(f"{path}\\data\\img\\{user_id}")
        except Exception as e:
            pass
        finally:
            image.save(f"{path}\\data\\img\\{user_id}\\{photo_name[:-4]}_{user_text}.jpg",
                       dpi=(300, 300),
                       optimize=False,
                       quality=100)