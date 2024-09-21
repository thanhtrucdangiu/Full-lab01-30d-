# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:19:10 2024

@author: ASUS
"""
n=int(input("Nhập số nguyên n (chẵn): "))
i = 2
S = 0
while i <= n:
    S= S + i
    i= i + 2
print("S= ",S)
