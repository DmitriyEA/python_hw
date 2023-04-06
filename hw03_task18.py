"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""

import random
number = int(input("Введите число: "))
num_list = []
k = 0
closest_num = -1
for i in range(15):
    num_list.append(random.randint(1, 101))
    min_d = max(num_list) - number

    if int(num_list[i]) == number:
        k += 1
for i in set(num_list):
    if abs(i - number) < min_d:
        min_d = abs(i - number)
        closest_num = i
print(f"{k} раз встречается в заданном списке число {number}")


print(f"максимально близкое число {closest_num}")

print(f"список {num_list}")