# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:03:47 2020

@author: User
"""


revenue = int(input("Введите вашу выручку: "))
expenses = int(input("Введите ваши издержки: "))
if revenue > expenses:
    profit = revenue - expenses
    print(f"Ваша прибыль составила: {profit}")
    rr = profit / revenue
    print(f"Ваша рентабельность выручки: {rr}")
    staff = int(input("Введите численность сотрудников вашей фирмы: ")) 
    profit_per_person = profit / staff
    print(f"Прибыль на одного сотрудника составила: {profit_per_person}")
elif expenses > revenue:
    losses = expenses - revenue
    print(f"Ваши убытки составили: {losses}")
elif revenue == expenses:
    print("Вы работаете в ноль")
    