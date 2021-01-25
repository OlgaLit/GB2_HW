# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:51:17 2021

@author: User
"""
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать 
дату в виде строки формата «день-месяц-год». В рамках класса реализовать 
два метода. Первый, с декоратором @classmethod, должен извлекать число, 
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором 
@staticmethod, должен проводить валидацию числа, месяца и года (например, 
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:

    def __init__(self, date):
        Date.str_date = date
    
    @classmethod
    def get_ddmmyy(cls):
        split_date = cls.str_date.split("-")
        cls.dd = int(split_date[0])
        cls.mm = int(split_date[1])
        cls.yy = int(split_date[2])
        return (cls.dd, cls.mm, cls.yy)
        
    @staticmethod
    def check():
        day = 1
        dd = Date.get_ddmmyy()[0]
        if dd in range(1, 32):
            day = dd
        
        month = 1      
        mm = Date.get_ddmmyy()[1]
        if mm in range(1, 13):
            month = mm
        
        year = 1990
        yy = Date.get_ddmmyy()[2]
        if yy > 2021:
            year = 2021
        elif yy < 1990:
            year = 1990
        else:
            year = yy
            
        return (day, month, year)   
    
    def __str__(self):
        return f"День: {Date.check()[0]}, месяц: {Date.check()[1]}, год: {Date.check()[2]}"

d = Date("32-10-2020")
print(d.get_ddmmyy()) 
print(d)
d1 = Date("15-02-1899")
print(d1)
d2 = Date("35-2-2058")   
print(d2)       
        
