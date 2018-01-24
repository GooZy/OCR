#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:17
# @Author  : Guo Ziyao
import glob
import subprocess

import cv2

from util import correct_angle
from util import recgnize
from util import show_img


def img_ocr(img_path, test=False):
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
    if test:
        show_img(img)
    # 识别
    return recgnize(img), img


def lets_go():
    duplicate = set()
    for each in glob.glob('/Users/guoziyao/Desktop/CR/cap1/*'):
        print each
        result = img_ocr(each)
        print result
        if result in duplicate:
            print 'OK: ' + result[0]
            break
        duplicate.add(result)


def train():
    index = 1
    for each in glob.glob('/Users/guoziyao/Desktop/CR/cap1/*'):
        result, img = img_ocr(each)
        file_name = 'train_data/%s.jpg' % index
        cv2.imwrite(file_name, img)
        subprocess.check_output('convert %s %s.tiff' % (file_name, file_name), shell=True)
        if index == 50:
            break
        index += 1


if __name__ == '__main__':
    # lets_go()
    # train()
    print img_ocr('/Users/guoziyao/Desktop/CR/cap1/im1224.png', test=True)[0]