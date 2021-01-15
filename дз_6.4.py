# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:36:34 2021

@author: User
"""
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие 
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, 
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, 
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен 
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar 
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) 
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ 
к атрибутам, выведите результат. Выполните вызов методов и также покажите 
результат.

"""
from random import randint
class Car:
    speed = randint(0, 160)
    color = "unknown"
    name = "unknown"
    is_police = False
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn_right(self):
        print("Машина повернула направо")
    def turn_left(self):
        print("Машина повернула налево")
    def show_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f"Текущая скорость: {self.speed} км/ч")
        else:
            print(f"Скорость превышена! Текущая скорость: {self.speed} км/ч")
class SportCar(Car):
    speed = randint(0, 200)
class WorkCar(Car):
    speed = randint(0, 80)
    def show_speed(self):
        if self.speed <= 40:
            print(f"Текущая скорость: {self.speed} км/ч")
        else:
            print(f"Скорость превышена! Текущая скорость: {self.speed} км/ч")
class PoliceCar(Car):
    is_police = True
    
rio = TownCar()
rio.color = "черный"
rio.name = "Kia Rio"
print(f"На радаре {rio.name}, цвет {rio.color}, {rio.speed} км/ч")
rio.go()
rio.turn_right()
rio.show_speed()

ferrari = SportCar()
ferrari.name = "Ferrari"
ferrari.color = "красный"
print(f"На радаре {ferrari.name}, цвет {ferrari.color}, {ferrari.speed} км/ч")
ferrari.go()
ferrari.turn_left()
ferrari.show_speed()

gaz = WorkCar()
gaz.name = "Газель"
gaz.color = "белый"
print(f"На радаре {gaz.name}, цвет {gaz.color}, {gaz.speed} км/ч")
gaz.stop()
gaz.go()
gaz.show_speed()

ford = PoliceCar()
ford.name = "Ford"
ford.color = "синий"
print(f"На радаре {ford.name}, цвет {ford.color}, {ford.speed} км/ч")
if ford.is_police:
    print("Внимание! Полиция!")
ford.go()
ford.turn_right()
ford.show_speed()



        
    