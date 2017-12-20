#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 09:18
# @Author  : Guo Ziyao
import cv2


def show_img(img):
    cv2.imshow('test', img)
    cv2.waitKey(0)