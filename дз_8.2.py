# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:32:36 2021

@author: User
"""
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления 
на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе 
пользователем нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
        
num = int(input("Введите делимое: ")) 
div = int(input("Введите делитель: "))
try:
    if div == 0:
        raise MyError("На ноль делить нельзя!")
except MyError as error:
    print(error)
else:
    print(num/div)
    
         
     
