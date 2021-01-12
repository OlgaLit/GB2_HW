# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:49:10 2021

@author: User
"""

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна 
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет средней 
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их 
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, 
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.

"""
outcomes = dict()
profits = []
with open("file7.txt", "r", encoding="utf-8") as f:
    for l in f.readlines():
        firm_info = l.split()
        profit = int(firm_info[2]) - int(firm_info[3])
        outcomes[firm_info[0]] = profit
        if profit > 0:
            profits.append(profit)
ave_profit_dict = {"average_profit": sum(profits)/len(profits)}
my_list = [outcomes, ave_profit_dict]

import json
with open("new_file7.json", "w") as new_f:
    json.dump(my_list, new_f)
       
    
