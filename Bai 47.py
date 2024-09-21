# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:58:12 2024

@author: ASUS
"""
a = None
max_t = 0
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y +9*z == 979:
                tong= x + y + z
                if tong > max_t:
                    max_t = tong
                    a = (x,y,z)
if a:
    print(f"Bộ nghiệm lớn nhất là: {a[0]},{a[1]},{a[2]} ")
    print(f"Tổng: {tong}")
else:
    print("không có tổng thảo mãn")