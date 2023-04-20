"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

list_len = int(input("Введите размер массива: "))
min_num = int(input("Введите минимальное число диапазона: "))
max_num = int(input("Введите максимальное число диапазона: "))

new_list = [random.randint(0, 10) for _ in range(list_len)]
print(new_list)

print("Индексы чисел, находящихся в заданном диапазоне: ")
for i in range(len(new_list)):
    if min_num <= new_list[i] <= max_num:
        print(i, end=" ")

