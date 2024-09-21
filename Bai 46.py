# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:39:39 2024

@author: ASUS
"""
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y + 9*z == 979:
                print (f"Bộ ngiệm số nguyên:{x},{y},{z}")
