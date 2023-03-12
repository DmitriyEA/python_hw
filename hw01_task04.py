"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""

items_total = int(input("Введите количество сделанных журавликов: "))

# x + x + 2(x + x) = items_total -> 6x = items_total

if items_total > 0 and items_total % 6 == 0:
    print(f"Петя и Сережа сделали по {items_total // 6} шт., а Катя сделала {items_total // 6 * 4} шт.")
else:
    print("Введено неверное количество журавликов.")