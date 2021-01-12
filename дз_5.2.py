# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:56:35 2021

@author: User
"""
"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open("file2.txt", "r", encoding="utf-8")
as_list = f.readlines()
print(f"Количество строк в файле: {len(as_list)}")
f.seek(0)
line_num = 0
for l in f.readlines():
    line_num += 1
    words = len(l.split())
    print(f"Количество слов в строке {line_num}: {words}")
f.close()    