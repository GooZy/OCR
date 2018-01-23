#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:17
# @Author  : Guo Ziyao
import glob

import cv2

from util import correct_angle
from util import recgnize
from util import show_img


def img_ocr(img_path):
    img = cv2.imread(img_path)
    # 放大
    h, w = img.shape[: 2]
    img = cv2.resize(img, None, fx=256.0/w, fy=256.0/w, interpolation=cv2.INTER_CUBIC)
    # 灰度
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show_img(gray_img)
    # 二值
    ret, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # show_img(binary_img)
    # 倾斜矫正
    img = correct_angle(binary_img)
    # show_img(img)
    # 识别
    return recgnize(img)


if __name__ == '__main__':
    duplicate = set()
    for each in glob.glob('/Users/guoziyao/Desktop/CR/cap1/*'):
        result = img_ocr(each)
        print ('%s: ' + result) % each
        if result in duplicate:
            print 'OK: ' + result
            break
        duplicate.add(result)