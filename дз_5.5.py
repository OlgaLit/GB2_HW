# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:31:41 2021

@author: User
"""

"""
5. Создать (программно) текстовый файл, записать в него программно набор 
чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел 
в файле и выводить ее на экран.
"""
f = open("file5.txt", "w")
for x in range(1, 50, 6):
    f.write(str(x)+" ")
f = open("file5.txt", "r")    
content = [int(x) for x in f.read().split()]
print(sum(content))