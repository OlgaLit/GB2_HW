# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:45:44 2021

@author: User
"""
"""
5. Реализовать формирование списка, используя функцию range() и возможности 
генератора. В список должны войти четные числа от 100 до 1000 (включая 
границы). Необходимо получить результат вычисления произведения всех 
элементов списка.
Подсказка: использовать функцию reduce().

"""
from functools import reduce
my_list = [d for d in range(100, 1001, 2)]
res = reduce(lambda el1, el2: el1 * el2, my_list)
print(res, my_list)