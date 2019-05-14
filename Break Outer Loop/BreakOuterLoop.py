# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:37:34 2019

@author: kWX596514
"""


for i in range(10):
    for j in range(10):
        x = i * j
        print(x)
        if x > 50:
            break
    else:
        continue
    break
