# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:06:03 2024

@author: ASUS
"""
so = int(input("Nhập số:"))
chuso = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
if 0<= so <= 9:
    print(chuso[so])
else:
    print("Không đọc được.")
