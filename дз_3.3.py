# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:01:32 2021

@author: User
"""
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""
def my_func(a, b, c):
    max2 = [a, b, c]
    max2.sort(reverse=True)
    return(max2[0] + max2[1])
