# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:33:26 2024

@author: ASUS
"""
n=int(input("Nhập số n: "))
i = 1
S = 0
while i <= n:
    S= S + 1/(2*i)
    i= i + 1
print("S= ",S)
