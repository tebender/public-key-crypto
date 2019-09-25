# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:34:10 2019

@author: Tim Bender
"""

import random

# helper function used to remove powers of two from a number a
def removePowTwo(a):
    i = 0
    while (a % 2 == 0):
        a = a // 2
        i = i + 1
    return [a, i]

#begin compositeness testing
x = int(input("Input an odd number you would like to test for compositeness "))
k = int(input("Input desired number of trials "))

i = 0
while (i < k):
    r = random.randint(1, x - 1)
    list = removePowTwo(x - 1)
    m = list[0]
    p = list[1]
    b = pow(r, int(m), x)
    if (b != 1):
        j = 0
        while(j < p):
            if (b == x - 1):
                break
            b = pow(b, 2, x)
            j = j + 1
        if (j == p):
            print(x, "is a composite number")
            break
    i = i + 1

if (i == k):
    print(x, "may be a prime number")