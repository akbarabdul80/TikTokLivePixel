class Position(object):
    window_x, window_y, window_x2, window_y2, \
        p_btn_x, p_btn_y, p_btn_key_x, p_btn_key_y, \
        p_et_x, p_et_y, p_et_key_x, p_et_key_y, \
        p_btn_next_x, p_btn_next_y, p_btn_close_x, p_btn_close_y, \
        p_btn_close_e_x, p_btn_close_e_y = \
        0, 0, 0, 0, \
            0, 0, 0, 0, \
            0, 0, 0, 0, \
            0, 0, 0, 0, \
            0, 0


def make_position(window_x, window_y, window_x2, window_y2):
    position = Position()
    position.window_x = window_x
    position.window_y = window_y
    position.window_x2 = window_x2
    position.window_y2 = window_y2

    # Button
    p_btn_x, p_btn_y = window_x2 - 72, window_y2 - 118
    p_btn_key_x, p_btn_key_y = p_btn_x, p_btn_y - 251
    position.p_btn_x = p_btn_x
    position.p_btn_y = p_btn_y

    position.p_btn_key_x = p_btn_key_x
    position.p_btn_key_y = p_btn_key_y

    position.p_btn_next_x = (window_x + window_x2) / 2
    position.p_btn_next_y = p_btn_y

    position.p_btn_close_x = window_x2 - 30
    position.p_btn_close_y = window_y2 - 408

    position.p_btn_close_e_x = window_x2 - 393
    position.p_btn_close_e_y = window_y2 - 386

    # Position Edit Text
    p_et_x, p_et_y = p_btn_x - 194, p_btn_y
    p_et_key_x, p_et_key_y = p_et_x, p_btn_y - 251
    position.p_et_x = p_et_x
    position.p_et_y = p_et_y
    position.p_et_key_x = p_et_key_x
    position.p_et_key_y = p_et_key_y

    return position
