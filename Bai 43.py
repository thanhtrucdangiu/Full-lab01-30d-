# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:26:58 2024

@author: ASUS
"""
n=int(input("Nhập số n : "))
i = 1
S = 0
while i <= n:
    S= S + i/(i+1)
    i= i + 1
print("S= ",S)
