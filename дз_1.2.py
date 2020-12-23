# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:43:53 2020

@author: User
"""


t = int(input("Введите время: "))
hours = t//3600
minutes =  (t % 3600) // 60
sec = (t % 3600) % 60
print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")
