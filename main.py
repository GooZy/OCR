#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:17
# @Author  : Guo Ziyao
import cv2

from util import show_img


def img_cr(img_path):
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show_img(gray_img)
    ret, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)
    show_img(binary_img)


if __name__ == '__main__':
    img_cr('test/im0.png')