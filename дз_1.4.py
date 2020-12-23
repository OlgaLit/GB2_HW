# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:41:42 2020

@author: User
"""


number = input("Введите число: ")
len_n = len(number)
max_i = 0
while len_n != 0:
    if int(number[len_n-1]) > max_i:
        max_i = int(number[len_n-1])
    len_n -= 1
print(max_i)    