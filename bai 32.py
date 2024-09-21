# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:23:31 2024

@author: ASUS
"""
s= float(input("nhập số km: "))
if s <= 1:
    st= s * 15000
if 2 <= s <= 5:
    st= ((s-1) * 13500) + 15000
if s >= 6:
    st= (15000 + ( 4*  13500 ) + (s-5)*11000)
if s > 120:
    st= (15000 + (4 * 13500) + (s-5)*11000)*0.9
print ("so tien phai tra la: ",st)