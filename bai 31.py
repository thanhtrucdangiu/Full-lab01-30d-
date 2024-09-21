# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:19:52 2024

@author: ASUS
"""
a=int(input("nhập số nguyên a: "))
b=int(input("nhập số nguyên b: "))
c=int(input("nhập số nguyên c: "))
if a+b>c or a+c>b or b+c>a:
    if a==b==c:
        print ("đây là tam giác đều")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("đây là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2== a**2:
        print ("đây là tam giác vuông")
    else:
        print("đây là tam giác thường")
else:
    print("đây không phải là tam giác")
        
