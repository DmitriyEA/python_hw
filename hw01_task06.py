"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным
номером, где сумма первых трех цифр равна сумме последних трех.
Вам требуется написать программу, которая проверяет счастливость билета.
"""

input_number = int(input("Введите шестизначный номер билета: "))

if 99999 < input_number < 1000000:
    print()
    print("Проверка:")
    print(f"{input_number // 100000} {input_number // 10000 % 10} {input_number // 1000 % 10}"
          f"     {input_number // 100 % 10} {input_number // 10 % 10} {input_number % 10}")
    print(f"{input_number // 100000 + input_number // 10000 % 10 + input_number // 1000 % 10}"
          f"           {input_number // 100 % 10 + input_number // 10 % 10 + input_number % 10}")

    if (input_number // 100000 + input_number // 10000 % 10 + input_number // 1000 % 10) == (input_number // 100 % 10 + input_number // 10 % 10 + input_number % 10):
        print("Билет счастливый")
    else:
        print()
        print("Билет несчастливый.")
else:
    print()
    print("Ошибка. Введите шестизначный номер")
