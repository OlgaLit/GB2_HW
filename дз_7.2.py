# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:12:37 2021

@author: User
"""
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь 
определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост 
(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для 
пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих 
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные 
на этом уроке знания: реализовать абстрактные классы для основных классов 
проекта, проверить на практике работу декоратора @property.

"""
from abc import ABC, abstractmethod

class AbstractCoat(ABC):
    @abstractmethod
    def usage(self):
        pass
    
class AbstractSuit(ABC):
    @abstractmethod
    def usage(self):
        pass

class MyCoat(AbstractCoat):
    def __init__(self, size):
        self.size = size
        
    @property    
    def usage(self):
        return self.size / 6.5 + 0.5

class MySuit(AbstractSuit):
    def __init__(self, height):
        self.height = height
        
    @property    
    def usage(self):
        return self.height * 2 + 0.3


s = int(input("Введите размер пальто: "))
coats = int(input("Введите количество пальто этого размера: "))
h = int(input("Введите рост для костюмов: "))
suits = int(input("Введите количество костюмов для этого роста: "))
coat1 = MyCoat(s)
suit1 = MySuit(h)
total_usage = coats * coat1.usage  + suits * suit1.usage
print(f"Общий расход ткани на {coats} пальто размера {s} и {suits} костюмов роста {h} составляет {total_usage}")    

    
    
    