# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:41:24 2021

@author: User
"""
"""
3. Создать текстовый файл (не программно), построчно записать фамилии 
сотрудников и величину их окладов. Определить, кто из сотрудников имеет 
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет 
средней величины дохода сотрудников.
"""

f = open("file3.txt", "r", encoding="utf-8")
below_20000 = []
salaries = []
for l in f.readlines():
    line = l.split()
    salaries.append(int(line[1]))
    if int(line[1]) < 20000:
        below_20000.append(line[0])
f.close()
print(f"Сотрудники с окладом ниже 20 тыс.: {', '.join(below_20000)}")
print(f"Средний доход сотрудников: {sum(salaries)/len(salaries)}")       
    
    