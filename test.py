import time

from pynput.mouse import Button

from data.status_enum import Status
from ext.emulator_ext import take_screenshot, insert_answer, click_btn_next
from ext.keyboard_mouse_ext import move_pointer, action_click, write_word
from ext.platform_ext import get_dir

position = take_screenshot(get_dir())

print("Move to Emulator")
move_pointer(position.window_x, position.window_x)
action_click(Button.left)

status = insert_answer("tuang air", position)

if status == Status.SUCCESS:
    print("Success")
    click_btn_next(position)
elif status == Status.FAILED:
    print("Failed")
elif status == Status.DIALOG:
    print("Dialog")
elif status == Status.DIALOG_EXTRA_LIFE:
    print("Dialog Extra")
# write_word("Akbar")
# time.sleep(0.2)
# print("Move to Btn Key")
# move_pointer(position.p_btn_x, position.p_btn_y)
# action_click(Button.left)
#
# move_pointer(position.p_btn_close_x, position.p_btn_close_y)
# #
#
# time.sleep(4)
# write_word("alas kaki")
# time.sleep(2)
# print("Move to Btn Key1")
# move_pointer(position.p_btn_x, position.p_btn_y)
# action_click(Button.left)
#
# time.sleep(2)
# print("Move to Btn next")
# move_pointer(position.p_btn_next_x, position.p_btn_next_y)
# action_click(Button.left)
#
# time.sleep(2)
# print("Move to Btn close")
# move_pointer(position.p_btn_close_x, position.p_btn_close_y)
# action_click(Button.left)
