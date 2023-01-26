import numpy as np
from PIL import Image

from ext.image_ext import rgb_to_hex
from ext.platform_ext import get_dir

# Open the image
img = Image.open(get_dir())

# Get the pixel array
pixels = np.array(img)

# Get the shape of the image
height, width, channels = pixels.shape

print(height)
print(width)

print(rgb_to_hex((1, 54, 49)))

# Iterate over the pixels and get their coordinates
# for i in range(height):
#     for j in range(width):
#         Get the pixel coordinates
# x, y = j, i
# Get the pixel value
# pixel = pixels[i, j]
# print(f'Pixel at ({x}, {y}): {pixel}')
