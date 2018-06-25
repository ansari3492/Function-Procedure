# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:35:27 2018

@author: Lenovo
"""

import ast

addition = 0

user_list = input()

userlist_dict = ast.literal_eval(user_list)


list_predifined = [13,14,17,18,19]


for i in userlist_dict.values():
    if i in list_predifined:
        addition = addition+0
    else:
        addition = addition+i


print("addition of values are : - ", addition)
        


    
    