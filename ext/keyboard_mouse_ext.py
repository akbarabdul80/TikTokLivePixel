import time
import pyautogui
from pynput.mouse import Button, Controller

mouse = Controller()


#
# while True:
#     print('Now we have moved it to {0}'.format(mouse.position))

def move_pointer(x, y):
    time.sleep(0.5)
    mouse.position = (x, y)


def action_click(btn: Button):
    mouse.press(btn)
    time.sleep(0.5)
    mouse.release(btn)


def double_click(btn: int):
    mouse.click(btn, 2)


def write_word(world: str):
    pyautogui.press("backspace", presses=30)
    pyautogui.typewrite(world)

# # Set pointer position
# mouse.position = (1083, 838)
# print('Now we have moved it to {0}'.format(
#     mouse.position))
#
# # Move pointer relative to current position
# # mouse.move(5, -5)
#
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)
