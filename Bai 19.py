# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:58:26 2024

@author: ASUS
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
sonhonhat = a
if b < sonhonhat:
    sonhonhat = b
if c < sonhonhat:
    sonhonhat = c
if d < sonhonhat:
    sonhonhat = d
print("Số nhỏ nhất là:",sonhonhat)

