# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:20:42 2024

@author: ASUS
"""
a=int(input("Nhạp so a"))
b=int(input('Nhap so b'))
c = int(input("Nhap so c"))
if a>b:
    a,b=b,c
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)