# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:43:17 2024

@author: ASUS
"""
import math
n=int(input("nhập số nguyên n: "))
sochinhphuong = math.sqrt(n)
a=int(sochinhphuong)
kq= a**a
if n == kq:
    print("đây là số chính phương",n)
else:
    print ("đây không phải là số chính phương")