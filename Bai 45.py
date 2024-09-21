# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:45:30 2024

@author: ASUS
"""
x=int(input("nhap so nguyen N: "))
n=int(input("nhap so nguyen x: "))
i=1
s1=0 
s2=0
while i<=n:
    s1 = s1 + i
    s2 = s2 + (x**i)/s1
    i = i + 1
print("tong la: ",s2)