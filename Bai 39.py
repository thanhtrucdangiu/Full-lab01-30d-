# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:30:24 2024

@author: ASUS
"""
n=int(input("Nhập số n: "))
i = 1
S = 0
while i <= n:
    S= S + 1/i
    i= i + 1
print("S= ",S)
