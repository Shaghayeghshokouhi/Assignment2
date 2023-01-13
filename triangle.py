# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:32:34 2023

@author: 2022
"""

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

if c<a+b and a<c+b and b<c+a:
    result = "correct"
else : 
    result = "incorrect"
    
print(result)   
