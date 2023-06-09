"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
2 2
4
"""

def recurs_sum(a, b):
    if b == 0:
        return a
    return 1 + recurs_sum(a, b - 1)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"{num1} + {num2} = {recurs_sum(num1, num2)}")