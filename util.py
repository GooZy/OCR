#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:18
# @Author  : Guo Ziyao
import cv2
import numpy as np
from PIL import Image
import pytesseract


def show_img(img):
    """
    显示图像，按任意键退出
    """
    cv2.imshow('test', img)
    cv2.waitKey(0)


def correct_angle(img):
    """
    图像倾斜矫正。找到外接矩形，然后取两条宽的中点算斜率，求倾斜角度
    :img: 二值化图像
    :return: 返回图像对象
    """
    blur = cv2.GaussianBlur(img, (51, 51), 0)
    ret, binary_img = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    edges = cv2.Canny(binary_img, 100, 200)
    image, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index = 0
    for each in contours:
        point = cv2.minAreaRect(each)[1]
        if point[1] != 0 and point[0] != 0:
            break
        index += 1
    rect = cv2.minAreaRect(contours[index])
    # angle = rect[2]
    # print angle
    points = cv2.boxPoints(rect)
    left, right, up, down = (1000, 0), (-1000, 0), (0, 1000), (0, -1000)
    for each in points:
        x, y = each
        if y <= up[1]:
            up = (x, y)
        if y >= down[1]:
            down = (x, y)
        if x <= left[0]:
            left = (x, y)
        if x >= right[0]:
            right = (x, y)
    # 如果本身水平
    if up[0] == down[0]:
        return img
    # print up, down, left, right
    # cv2.rectangle(img, up, down, 1)
    # show_img(img)
    if up[0] > down[0]:
        x1, y1 = (up[0] + right[0]) / 2.0, (up[1] + right[1]) / 2.0
        x2, y2 = (down[0] + left[0]) / 2.0, (down[1] + left[1]) / 2.0
        angle = np.arctan((y1 - y2) / (x1 - x2)) * 180 / np.pi
    else:
        x1, y1 = (up[0] + left[0]) / 2.0, (up[1] + left[1]) / 2.0
        x2, y2 = (down[0] + right[0]) / 2.0, (down[1] + right[1]) / 2.0
        angle = np.arctan((y1 - y2) / (x1 - x2)) * 180 / np.pi
    rows, cols = img.shape[: 2]
    # print angle
    M = cv2.getRotationMatrix2D((int(rows / 2), int(cols / 2)), angle, 1)
    img = cv2.warpAffine(img, M, (rows, cols), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # cv2.drawContours(img, contours, 0, (0, 0, 255), 1)
    return img


def recgnize(img, lang):
    cv2.imwrite('tmp.jpg', img)
    # pytesseract 0.1.8
    # http://hellosure.github.io/ocr/2014/10/11/tesseract-ocr
    # -psm 7: only recognize one line
    code = pytesseract.image_to_string(cv2.imread('tmp.jpg'), config="-psm 7 -c tessedit_char_whitelist='abcdefghijklmnopqrstuvwxyz' -l %s" % lang)
    return code


if __name__ == '__main__':
    img = cv2.imread('test/im0.png')
    h, w = img.shape[: 2]
    img = cv2.resize(img, None, fx=256.0 / w, fy=256.0 / w, interpolation=cv2.INTER_CUBIC)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    show_img(correct_angle(binary_img))
