# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:06:33 2019

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

def millerRabinCompositeTest(x, k):
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
                return True
        i = i + 1
    
    return False


composite = True
x = 0
while (composite):
    x = random.randrange(10**149, 10**150)
    composite = millerRabinCompositeTest(x, 20)
print(x, "is a prime with", len(str(x)), "digits")