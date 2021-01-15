# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:51:05 2021

@author: User
"""
"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут 
color (цвет) и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, 
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и 
вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его 
нарушении выводить соответствующее сообщение и завершать скрипт.

"""
import time

class TrafficLight:
    __color = ""
    def running(self):
        start = time.time()
        seq = []
        self.__color = "красный"
        print(f"Горит {self.__color}")
        seq.append(self.__color)
        while time.time() <= start + 7:
            pass
        self.__color = "желтый"
        print(f"Горит {self.__color}")
        seq.append(self.__color)
        while time.time() <= start + 7 + 2:
            pass
        self.__color = "зеленый"
        print(f"Горит {self.__color}")
        seq.append(self.__color)
        while time.time() <= start + 7 + 2 + 5:
            pass
        return seq     

t = TrafficLight()
correct_seq = ['красный', 'желтый', 'зеленый']
for _ in range(2):
    s = t.running()
    if s != correct_seq:
        print("Светофор неисправен")
        break

                      
        