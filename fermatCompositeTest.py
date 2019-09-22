# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:12:14 2019

@author: Tim Bender
"""
import random

x = int(input("Input a number to test for compositeness "))
k = int(input("Input desired number of trials "))

i = 0;

while (i < k):
    r = random.randint(1 , x - 1)
    y = pow(r, x - 1, x)
    if (y != 1):
        print(x, "is a composite number")
        break
    i = i + 1
if (i == k):
    print(x, "may be prime")