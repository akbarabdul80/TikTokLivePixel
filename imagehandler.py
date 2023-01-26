import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
import pytesseract
from ext import image_ext

bounding_box = {'top': 80, 'left': 1350, 'width': 500, 'height': 1000}

sct = mss()
# for i in threshInv:
#     print(i)
#     if 255 in i:
#         print("putih")
#     else:
#         print("hitam")

# for y in range(0, h):
#     for x in range(0, w):
#         # threshold the pixel
#         threshInv[y, x] = 255 if threshInv[y, x] >= T else 0
#         print(threshInv[y, x])

# cv2.imshow('crop', threshInv)
#
while True:
    # sct_img = np.array(sct.grab(bounding_box))

    # crop_img = sct_img[500:600, 10:500]
    # gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    # (T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # cv2.imshow('crop', sct_img)
    last_time = time.time()
    sct_img = np.array(sct.grab(bounding_box))

    h, w = sct_img.shape[:2]

    start_point = (10, 500)
    end_point = (500, 600)
    crop_img = sct_img[500:600, 10:400]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    (D, threshOcr) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('OCR', threshOcr)
    string_image = pytesseract.image_to_string(threshOcr)

    print(string_image)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    (T, threshInv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    count = 0
    tmp = False
    white = image_ext.change_color(sct_img)
    # cv2.imshow('white', white)

    for i in threshInv:
        for x in i:
            if x == 255:
                if not tmp:
                    count += 1
                tmp = True
            else:
                tmp = False
        if 255 in i:
            break
    cv2.imshow('crop', threshInv)
    print(f'Jumlah Kotak {count}')
    # cv2.rectangle(sct_img, start_point, end_point, (255, 0, 0), 2)
    # cv2.imshow('screen', sct_img)
    # # print("fps: {}".format(1 / (time.time() - last_time)))
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
