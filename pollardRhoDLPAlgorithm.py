# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:03:40 2019

@author: Tim Bender
"""
import math

# method taken from Wikipedia
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# method used to create pseudorandom map
def f(t, a, b, n, g):
    if (t[0] % 3 == 0):
        t[0] = (t[0]**2 % g)
        t[1] = (t[1]*2 % n)
        t[2] = (t[2]*2 % n)
    elif (t[0] % 3 == 1):
        t[0] = (t[0]*b % g)
        t[2] = ((t[2] + 1) % n)
    else:
        t[0] = (t[0]*a % g)
        t[1] = ((t[1] + 1) % n)
    return t

# begin script
b = int(input("Input number to take Log of: "))
a = int(input("Input the base of the Log: "))
n = int(input("Input the order of the base in the group: "))
g = int(input("Input modulous of the group: "))


x = [1, 0, 0]
y = [1, 0, 0]
x = f(x, a, b, n, g)
y = f(y, a, b, n, g)
y = f(y, a, b, n, g)

count = 1

while (x[0] != y[0]):
    x = f(x, a, b, n, g)
    y = f(y, a, b, n, g)
    y = f(y, a, b, n, g)
    count = count + 1
print("Match found on iteration", count)

i = (x[1] - y[1]) % n
j = (y[2] - x[2]) % n

if (math.gcd(j, n) == 1):
    jinv = xgcd(j, n)[1] % n
    print("Log("+ str(b) + ") is", (i*jinv) % n)
else:
    print("Algorithm failed, could not find an inverse for", j , "mod", g)