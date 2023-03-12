"""
Найдите сумму цифр трехзначного числа.
"""

input_number = int(input("Введите трехзначное число: "))

if 99 < input_number < 1000:
    print(f"{input_number // 100} + {input_number // 10 % 10} + {input_number % 10}"
          f" = {input_number // 100 + input_number // 10 % 10 + input_number % 10}")
else:
    print("Вы ввели не трехзначное число.")
