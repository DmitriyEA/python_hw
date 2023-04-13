"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def num1_deg_num2(a, b):
    if b == 0:
        return 1
    return a * num1_deg_num2(a, b - 1)


num1 = int(input("Введите число: "))
num2 = int(input("Введите степень: "))
print(f"{num1} ^ {num2} = {num1_deg_num2(num1, num2)}")
