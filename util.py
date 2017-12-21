#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:18
# @Author  : Guo Ziyao
import cv2
import numpy as np


def show_img(img):
    """
    显示图像，按任意键退出
    """
    cv2.imshow('test', img)
    cv2.waitKey(0)


def correct_angle(img):
    """
    图像倾斜矫正
    :return: 返回图像对象
    """
    return img


if __name__ == '__main__':
    img = cv2.imread('test/im0.png')
    h, w = img.shape[: 2]
    img = cv2.resize(img, None, fx=256.0 / w, fy=256.0 / w, interpolation=cv2.INTER_CUBIC)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    show_img(correct_angle(binary_img))
