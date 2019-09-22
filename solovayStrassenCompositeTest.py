# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:30:48 2019

@author: Tim Bender
"""
import random

# helper function used to remove powers of two from the numerator of the
# jacobi symbol
def removePowTwo(a, n):
    i = 0
    s = 1
    while (a % 2 == 0):
        a = a / 2
        i = i + 1
    if (i % 2 == 1):
        if (n % 8 == 3 or n % 8 == 5):
            s = s * (-1)
    return [a, s]

# function meant to find the jacobi symbol of two non negative integers,
# a mod n
def findJacobi(a, n):
    state = 1
    while (n > 3):
        list = removePowTwo(a, n)
        a = list[0]
        state = state * list[1]
        if (a == 1):
            break
        if (a % 4 == 3 and n % 4 == 3):
            state = state * (-1)
        temp = n % a
        n = a
        a = temp
    
    if (a == 1):
        return 1 * state
    elif(a == 0):
        return 0
    else:
        return -1 * state

#begin compositeness testing
x = int(input("Input an odd number you would like to test for compositeness "))
k = int(input("Input desired number of trials "))

i = 0
while (i < k):
    r = random.randint(1, x - 1)
    j = findJacobi(r, x)
    if (j == 0):
        print(x, "is a composite number")
        break
    p = int((x-1)/2)
    y = pow(r, p, x)
    if(y == x - 1):
        y = -1
    if (j != y):
        print(x, "is a composite number")
        break
    i = i + 1
if (i == k):
    print(x, "may be a prime number")