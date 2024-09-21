# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:42:36 2024

@author: ASUS
"""
a = float(input("nhap so nguyen a:"))
b = float(input("nhap so nguyen b:"))
c = float(input("nhap so nguyen c:"))
min = a
max = a
if b > max:
    max = b
if c > max:
    max = c
if b < min:
    min = b
if c < min:
    min = c
print("so lon nhat: ",max )
print("số nhỏ nhất: ",min)