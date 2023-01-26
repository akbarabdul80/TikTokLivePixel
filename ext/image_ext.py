from mss import mss
import numpy as np
import cv2

bounding_box = {'top': 80, 'left': 1350, 'width': 500, 'height': 1000}
sct = mss()


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def count_field(img):
    count = 0
    tmp = False
    for i in img:
        for x in i:
            if x == 255:
                if not tmp:
                    count += 1
                tmp = True
            else:
                tmp = False
        if 255 in i:
            break
    return count


def change_color(img, count):
    h, w = img.shape[:2]
    tmp = False
    tmp_count = 0
    for height in range(h):
        for width in range(w):
            print(img[height, width])
            pixel = img[height, width]
            if pixel == 255:
                if not tmp:
                    tmp_count += 1
                tmp = True
            else:
                img[height, width] = 255
                tmp = False
        if tmp_count == count:
            break
    return img


# sct_img = np.array(sct.grab(bounding_box))
# crop_img = sct_img[500:600, 10:400]
# gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# (T, threshInv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#
# white = change_color(threshInv, count_field(gray))
# while True:
#     # print(count_field(white))
#     cv2.imshow('white', white)
#
#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break
