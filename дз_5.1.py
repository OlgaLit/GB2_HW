# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:12:43 2021

@author: User
"""

"""
1. Создать программно файл в текстовом формате, записать в него построчно 
данные, вводимые пользователем. Об окончании ввода данных свидетельствует 
пустая строка.
"""
with open('file1.txt', 'w') as my_file:
    while True:
        user_line = input("Введите данные: ")
        my_file.write(user_line+"\n")
        if not user_line:
            break
# дальше для проверки содержимого файла:        
out = open("file1.txt", "r")
print(out.read())