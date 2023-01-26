import os
import time

import pygetwindow
import pyautogui
from PIL import Image
from pynput.mouse import Button

from ext.keyboard_mouse_ext import move_pointer, action_click, double_click, write_word
from ext.platform_ext import get_dir

titles = pygetwindow.getAllTitles()

print(titles)

dir = get_dir()
x1, y1, width, height = pygetwindow.getWindowGeometry(
    "qemu-system-x86_64 Android Emulator - Pixel_3a_API_33_x86_64:5554")
x2 = x1 + width
y2 = y1 + height

print(y2)
print(dir)
pyautogui.screenshot(dir)
im = Image.open(dir)
im = im.crop((x1, y1, x2, y2))
im.save(dir)

# Position Button
p_btn_x, p_btn_y = x2-72, y2-118
p_btn_key_x, p_btn_key_y = p_btn_x, p_btn_y-251

print(p_btn_y)
print(p_btn_key_y)

# Position Edit Text
p_et_x, p_et_y = p_btn_x-194, p_btn_y
p_et_key_x, p_et_key_y = p_et_x, p_btn_y-251
# im.show(dir)

# move_pointer(p_btn_x, p_btn_y)
# print("Button")
# action_click(Button.left)
# action_click(Button.left)
time.sleep(3)

print("Move to Et")
move_pointer(x1, y1)
# action_click(Button.left)
# time.sleep(2)
action_click(Button.left)
#
# move_pointer(p_et_x, p_et_y)
# action_click(Button.left)
#
# time.sleep(0.2)
# print("Move to Et Key")
# move_pointer(p_et_key_x, p_et_key_y)
# action_click(Button.left)

write_word("Akbar")

time.sleep(0.2)
print("Move to Btn Key")
move_pointer(p_btn_x, p_btn_y)
action_click(Button.left)
