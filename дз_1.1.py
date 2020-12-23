# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:44:47 2020

@author: User
"""


name = ''
age = 0
intro = "Здравствуй, малыш! Я Дед Мороз."
print(intro)
name = input("Как тебя зовут?  ")
age = int(input("Скольке тебе лет?  "))
if age < 10:
    print("С Новым годом, {}!".format(name))
else:
    print("Такой большой, а всё ещё веришь в Деда Мороза?!")    