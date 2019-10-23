# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:58:54 2019

@author: Tim Bender
"""
# method taken from Wikipedia
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

b = int(input("Input number to take Log of: "))
a = int(input("Input the base of the Log: "))
n = int(input("Input the order of the base in the group: "))
g = int(input("Input the modulous of the group: "))

m = int(n**.5) + 1
l1 = []
l2 = []

for i in range(m):
    l1.append((i, (a**(m*i)) % g))

# need to find a inverse in the group
ainv = xgcd(a, g)[1] % g

for i in range(m):
    l2.append((i, (b*ainv**(i)) % g))
    
for i in l1:
    for j in l2:
        if (i[1] == j[1]):
            print("Log("+ str(b) + ") is", (m*i[0] + j[0]) % n)

print("Program terminated")