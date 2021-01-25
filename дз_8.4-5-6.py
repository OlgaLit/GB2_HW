# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:06:08 2021

@author: User
"""
"""
4-5-6. «Склад оргтехники»
"""

class Warehouse:
    keep = dict()
    def __init__(self):
        print("Склад создан")

    def to_keep(self, *items):        
        for i in items:
            self.keep[i.brand] = i.qty    
        return self.keep
         
            
class OfficeEquipment:
    total = 0
    def __init__(self, brand, quantity):
        self.brand = brand
        self.qty = quantity
    @classmethod
    def totals(cls, *pos):          
        for el in pos: 
            cls.total += el.qty
        return cls.total
        
class Printer(OfficeEquipment):
    def __init__(self, brand, quantity, plotter=False):
        super().__init__(brand, quantity)
        self.plotter = plotter    
                                 
class Scanner(OfficeEquipment):
    def __init__(self, brand, quantity, speed):
        super().__init__(brand, quantity)
        self.speed = speed
    def get_speed(self):
        return self.speed
        
class Copier(OfficeEquipment):
    def __init__(self, brand, quantity, **kwargs):
        super().__init__(brand, quantity)
        for key in kwargs:
            setattr(self, key, kwargs[key])
    
class InputError(Exception):
    def __init__(self, txt):
        self.txt = txt


w = Warehouse()        
try:
    p = Printer("Canon","пять")
    if p.qty is not int:
        raise InputError(f"Неверно введено количество {p.brand}")
except InputError as error:
    print(error)
       
p = Printer("Canon", 5, plotter=True)
p1 = Printer("HP", 8)
s = Scanner("Sony",10, speed=100)
c =  Copier("xerox", 12, size='a4')

print(w.to_keep(p, p1, s, c))
print(OfficeEquipment.totals(p, p1, s, c))



        