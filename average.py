# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = input("please enter your name")
family = input("please enter your family")
a = float(input("enter the score"))
b = float(input("enter the score"))
c = float(input("enter the score"))
plus = a + b + c
average = plus / 3
if average >=18:
    print("greate")
elif 12<=average<17:
    print("normal")
elif average<12:
    print("fail")