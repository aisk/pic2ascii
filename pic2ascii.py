from typing import Tuple

import fire
from PIL import Image


WIDTH = 80
CHARS = "   ...',:;clodxkO0KXNWMMMM"


def pic2ascii(
    filename: str, *, reverse: bool = False, width=WIDTH, height=0, chars=CHARS
):
    chars = CHARS
    if reverse:
        chars = list(reversed(chars))
    output = ""
    image = Image.open(filename)
    size = getsize(image, width, height)
    image = image.resize(size)
    image = image.convert("L")
    pixs = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            output += chars[int(pixs[x, y] / 10)]
        output += "\n"
    print(output)


def getsize(image: Image.Image, width: int, height: int) -> Tuple[int, int]:
    """Calculate the target picture size"""
    s_width = image.size[0]
    s_height = image.size[1]
    t_width = width
    t_height = height
    if not t_height:
        t_height = (s_height * t_width) / s_width
        t_height = int(t_height * 0.4)
    t_size = (t_width, t_height)
    return t_size


if __name__ == "__main__":
    fire.Fire(pic2ascii)
