# Color Palette
# Created by Adrian Urbaniak / A-Rave-Mistake (2022)
# ----------
# Repo link: https://github.com/A-Rave-Mistake/Color_Palette
# Using GNU General Public License v3.0 - More info can be found in the 'LICENSE.md' file


from math import ceil
from random import randint
from typing import Tuple


cmyk_value = Tuple[float, float, float, float]
rgb_value = Tuple[int, int, int]


# check if string parameter is a valid HEX value
def is_hex_color(color: str) -> bool:
    import re
    check = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
    return True if check else False

# check if string parameter is a valid RGB value
def is_rgb_color(color: rgb_value) -> bool:
    cases = [val for val in color if val in range(0, 255)]
    return all(cases)

def hex_to_rgb(hex_value: str) -> str:
    hex = hex_value.lstrip('#')
    return str(tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4)))

def rgb_to_hex(rgb: rgb_value) -> str:
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

def random_rgb() -> rgb_value:
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def get_shade(rgb_color: rgb_value, scalar: float) -> cmyk_value:
    return rgb_to_cmyk(rgb_color[0], rgb_color[1], int(rgb_color[2] * scalar))

def rgb_to_cmyk(r: int, g: int, b: int) -> cmyk_value:
    RGB_SCALE = 255
    CMYK_SCALE = 100

    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,CMYK_SCALE]
    return clamp_cmyk(c * CMYK_SCALE), clamp_cmyk(m * CMYK_SCALE), clamp_cmyk(y * CMYK_SCALE), clamp_cmyk(k * CMYK_SCALE)

def clamp_cmyk(value: float):
    return float(min(ceil(value), 100))