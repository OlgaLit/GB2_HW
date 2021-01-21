# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:31:41 2021

@author: User
"""
"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
класса (метод __init__()), который должен принимать данные (список списков) 
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных 
в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы 
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции 
сложения двух объектов класса Matrix (двух матриц). Результатом сложения 
должна быть новая матрица.

"""


class Matrix:
    def __init__(self, param: list):
        self.param = param
    
    def __str__(self):
        return "\n".join(str(el) for el in self.param)
    
    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.param)):
            row = [el[0] + el[1] for el in list(zip(self.param[i], other.param[i]))]
            new_matrix.append(row) 
        return Matrix(new_matrix)
    
m1 = Matrix([[1,1,1],[2,2,2]])
print(m1)
m2 = Matrix([[3,3,3],[4,4,4]]) 
print(m1 + m2)               