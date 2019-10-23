# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:41:44 2019

@author: Tim Bender
"""
import math

n = int(input("Input a number to be factored: "))

x = 1
y = 1
p = 1
i = 0

while (p == 1):
    x = (x**2 + 1) % n
    y = ((y**2 + 1)**2 + 1) % n
    p = math.gcd(y - x, n)
    i = i + 1

if (p == n):
    print("The algorithm failed")
else:
    print(p, "is a factor of", n)
    print("It was found in", i, "iterations")