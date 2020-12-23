# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:26:09 2020

@author: User
"""


a = int(input("Результат 1-го дня: "))
b = int(input("Желаемый результат: "))
count = 1
while True:
    count +=1
    a = a + a*0.1
    a = round(a, 2)
    print(a)
    if a > b:
        break
print(f"Номер дня: {count}")    
