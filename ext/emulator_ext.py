import time

import cv2
import pyautogui
import pygetwindow
from PIL import Image
from pynput.mouse import Button

from data.position_data import make_position, Position
from data.status_enum import Status
from ext.image_ext import rgb_to_hex
from ext.keyboard_mouse_ext import write_word, move_pointer, action_click
from ext.platform_ext import get_dir


def take_screenshot(directory: str):
    x1, y1, width, height = pygetwindow.getWindowGeometry(
        "qemu-system-x86_64 Android Emulator - Pixel_3a_API_33_x86_64:5554")
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(directory)
    im = Image.open(directory)
    im = im.crop((x1, y1, x2, y2))
    im.save(directory)
    return make_position(x1, y1, x2, y2)


def check_is_true():
    directory = get_dir()
    take_screenshot(directory)
    image = cv2.imread(directory)

    color = image[758, 373]

    R = color[2]
    G = color[1]
    B = color[0]

    print(color)
    print(rgb_to_hex((3, 135, 122)))

    rgb = rgb_to_hex((R, G, B))
    if rgb == "f96908":
        return Status.FAILED
    elif rgb == '03877a':
        return Status.SUCCESS
    elif rgb == '013631':
        return Status.DIALOG_EXTRA_LIFE
    else:
        return Status.DIALOG


def insert_answer(question: str, position: Position):
    write_word(question)
    time.sleep(0.2)
    print("Move to Btn Key")
    move_pointer(position.p_btn_x, position.p_btn_y)
    action_click(Button.left)
    time.sleep(3)
    return check_is_true()


def click_btn_next(position: Position):
    time.sleep(0.2)
    move_pointer(position.p_btn_next_x, position.p_btn_next_y)
    action_click(Button.left)
