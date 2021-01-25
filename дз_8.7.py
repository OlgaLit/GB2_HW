# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:05:07 2021

@author: User
"""
"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число», реализуйте перегрузку методов сложения и умножения 
комплексных чисел. Проверьте работу проекта, создав экземпляры класса 
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
     
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumber(new_a, new_b)
    
    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.a * other.b + other.a * self.b
        return ComplexNumber(new_a, new_b)
    
    def __str__(self):
        return f"Ваше комплексное число: {self.a} + i*{self.b}"
    
n1 = ComplexNumber(2, 3)
n2 = ComplexNumber(7, 1.5)
print(n1 + n2) 
print(n1 * n2)   
        