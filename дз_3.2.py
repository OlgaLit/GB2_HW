# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:20:43 2021

@author: User
"""
"""
Реализовать функцию, принимающую несколько параметров, описывающих данные 
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. Реализовать 
вывод данных о пользователе одной строкой.
"""
def user_info(**kwargs):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    birth_year = input("Введите год рождения: ")
    city = input("Введите город проживания: ")
    email = input("Введите адрес электронной почты: ")
    phone = input("Введите телефон: ")
    return(f"Имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город проживания: {city}, адрес электронной почты: {email}, телефон: {phone}")

print(user_info())
    
