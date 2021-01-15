# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:02:06 2021

@author: User
"""
"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
   name, surname, position (должность), income (доход). Последний атрибут 
   должен быть защищенным и ссылаться на словарь, содержащий элементы: 
   оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать 
   класс Position (должность) на базе класса Worker. В классе Position 
   реализовать методы получения полного имени сотрудника (get_full_name) 
   и дохода с учетом премии (get_total_income). Проверить работу примера 
   на реальных данных (создать экземпляры класса Position, передать 
   данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = "John"
    surname = "Doe"
    position = "Director"
    _income = {"wage": 20000, "bonus": 5000}
    
class Position(Worker):
    def __init__(self, name, surname, pos, wage, bonus):
        Position.name = name
        Position.surname = surname
        Position.position = pos
        Position._income = {"wage": wage, "bonus": bonus}
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

employee1 = Position("Peter", "Pen", "Manager", 3000, 1000)
print(employee1.name, employee1.surname, employee1.position)
print(f"{employee1.get_full_name()} имеет общий доход ${employee1.get_total_income()}")    
empl2 = Position("Иван", "Иванов", "Инженер", 5000, 1500)
print(empl2.name, empl2.surname, empl2.position)
print(f"{empl2.get_full_name()} имеет общий доход ${empl2.get_total_income()}")    