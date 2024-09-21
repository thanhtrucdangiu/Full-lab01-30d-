# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:33:35 2024

@author: ASUS
"""
n=int(input("Nhập số n : "))
i = 1
S = 0
while i <= n:
    S= S + (2 * i + 1)/(2 * i +2)
    i= i + 1
print("S= ",S)
