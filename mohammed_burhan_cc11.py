# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:22:52 2018

@author: Lenovo
"""

import functools
number=[2,5,6,2,3]


def add():
    s=sum(number)
    return s
add()

def addition(x,y): return x+y
map(addition,range(0,10))
def multiply(x,y): return x*y
print(functools.reduce(multiply,number))
    
    
def largest():
    l=max(number)
    return l
largest()
def sorting():
    k=number.sort()
   
    return k
sorting()


