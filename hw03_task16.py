"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
записаны N целых чисел Ai. Последняя строка содержит число X.
"""

import random

num_len = int(input("Введите размер массива: "))
number = int(input("Введите число: "))

num_list = [random.randint(0, 10) for _ in range(num_len)]
print(num_list)
count = 0

for item in num_list:
    if item == number:
        count += 1
print(f"Число {number}, встречается в массиве {count} раз(а).")
