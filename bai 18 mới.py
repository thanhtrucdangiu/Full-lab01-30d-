# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:16:58 2024

@author: ASUS
"""
a=int(input("nhap gio thu nhat: "))
b=int(input("nhap phut thu nhat: "))
c=int(input("nhap giay thu nhat: "))
d=int(input("nhap gio thu hai: "))
e=int(input("nhap phut thu hai: "))
f=int(input("nhap giay thu hai: "))
s1=a*3600+b*60+c
s2=d*3600+e*60+f
s=s1+s2
tonggio=s//3600
tongphut=s%3600//60
tonggiay=s%3600%60
print(f"tong la: {tonggio} gio {tongphut} phut { tonggiay} giay")
if s1>s2:
    x=s1-s2
    hieugio=x//3600
    hieuphut=x%3600//60
    hieugiay=x%3600%60
    print(f"hieu la: {hieugio} gio {hieuphut} phut { hieugiay} giay")
else:
    print("hieu khong hop le")
