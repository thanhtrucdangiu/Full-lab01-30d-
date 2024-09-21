# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:34:18 2024

@author: ASUS
"""
n=int(input("nhap so nguyen duong N: "))
i=2
while i<n:
    if n%i==0:
        break
    i=i+1
if i==n:
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai la so nguyen to")

