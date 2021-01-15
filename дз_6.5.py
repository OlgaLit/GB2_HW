# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:48:23 2021

@author: User
"""
"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить 
в нем атрибут title (название) и метод draw (отрисовка). Метод выводит 
сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать 
переопределение метода draw. Для каждого из классов методы должен выводить 
уникальное сообщение. Создать экземпляры классов и проверить, что выведет 
описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pensil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")  

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

inst = Stationery("любой инструмент")
print(inst.title)
inst.draw()        
inst1 = Pen("ручка")        
print(inst1.title)
inst1.draw() 
inst2 = Pensil("карандаш")        
print(inst2.title)
inst2.draw()  
inst3 = Handle("маркер")        
print(inst3.title)
inst3.draw()    