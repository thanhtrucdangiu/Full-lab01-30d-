# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:49:19 2024

@author: ASUS
"""
while True:
    a=input("nhap so nguyen N: ")
    if a.isdigit():
        n=int(a)
        if n > 0:
            break
        else:
            print("so phai lon hon 0. Vui long nhap lai")
    else:
        print("so da nhap khong hop le. Vui long nhap lai")
print(f"cac uoc so cua {n} la :")
for i in range(1,n+1):
    if n%i ==0:
        print(i, end=' ')
