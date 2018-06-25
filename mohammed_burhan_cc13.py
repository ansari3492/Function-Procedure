# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:28:40 2018

@author: Lenovo
"""

n=5
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print('')