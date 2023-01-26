from ext.emulator_ext import take_screenshot
from ext.image_ext import rgb_to_hex
from ext.platform_ext import get_dir
import cv2
import numpy as np

position = take_screenshot(get_dir())

image = cv2.imread(get_dir())

color = image[758, 373]

R = color[2]
G = color[1]
B = color[0]

print(color)
print(rgb_to_hex((3, 135, 122)))

rgb = rgb_to_hex((R, G, B))
if rgb == "f96908":
    print("gagal")
elif rgb == '03877a':
    print("sukses")
else:
    print("dialog")
