# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:07:09 2021

@author: User
"""
"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться 
на русские. Новый блок строк должен записываться в новый текстовый файл.

"""
f = open("file4.txt", "r", encoding="utf-8")
d = {"One": "Один",
     "Two": "Два",
     "Three": "Три",
     "Four": "Четыре"}
for l in f.readlines():
    line = l.split()
    new_l = l.replace(line[0], d[line[0]])
    with open("new_file4.txt", "a", encoding="utf-8") as new_f:
        new_f.write(new_l)
f.close()        
with open("new_file4.txt", "a", encoding="utf-8") as new_f:
        print(new_f.readlines())       
        
    
