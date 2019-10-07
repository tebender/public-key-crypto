# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:31:22 2019

@author: Tim Bender
"""
import math

n = int(input("Input a number to be factored: "))
b = int(input("Choose a bound on iterations: "))
a = int(input("Choose a base (usually 2): "))

i = 2
while (i <= b):
    a = pow(a, i, n)
    d = math.gcd(a - 1, n)
    if (1 < d and d < n):
        print(d, "is a factor of", n)
        break
    i = i + 1

if (i > b):
    print("algorithm failed")