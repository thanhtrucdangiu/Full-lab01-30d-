# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:07:48 2024

@author: ASUS
"""
a = None
min_t = 999
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y +9*z == 979:
                tong= x + y + z
                if tong < min_t:
                   min_t = tong
                   a = (x,y,z)
if a:
    print(f"Bộ nghiệm nhỏ nhất là: {a[0]},{a[1]},{a[2]} ")
    print(f"Tổng: {min_t}")
else:
    print("không có tổng thảo mãn")
