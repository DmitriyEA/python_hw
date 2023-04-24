"""
Дополнить телефонный справочник.
"""

def main_menu():
    print()
    print("----------------------------")
    print("Главное меню")
    print("1 - Показать все контакты")
    print("2 - Создать новый контакт")
    print("3 - Найти контакт")
    print("4 - Изменить контакт")
    print("5 - Удалить контакт")
    print("6 - Выход")
    print("----------------------------")

def show_all():
    file = open("sample.txt", "r", encoding="UTF-8")
    data = file.readlines()
    file.close()
    print()
    for i in data:
        print(i)
    print()
    print("Для возврата в главное меню, введите цифру '0' ")

def add_contact():
    file = open("sample.txt", "a", encoding="UTF-8")
    data = input("Введите фамилию и имя, телефон и комментарий (через ;) ")
    data += "\n"
    file.write(data)
    file.close()
    print("Для возврата в главное меню, введите цифру '0' ")

def find_contact():
    find_string = input("Введите поисковый запрос: ")
    file = open("sample.txt", "r", encoding="UTF-8")
    data = file.readlines()
    file.close()
    print()
    for data_str in data:
        if find_string.lower() in data_str.lower():
            print("Найдена информация: ", data_str)
    print("Для возврата в главное меню, введите цифру '0' ")

def edit_contact():
    find_string = input("Введите поисковый запрос: ")
    replace_string = "Введите новую информацию: "
    file = open("sample.txt", "r", encoding="UTF-8")
    data = file.readlines()
    data_new = []
    for data_str in data:
        if find_string in data_str:
            print("Найдена информация: ", data_str)
            data_new.append(replace_string)
        else:
            data_new.append(data_str)
    file.close()
    file = open("sample.txt", "w", encoding="UTF-8")

def del_contact():
    del_string = input("Кого вы хотите удалить? Введите фамилию и имя: ")
    data = open("sample.txt", "r", encoding="UTF-8")
    result_data = []
    print()
    for line in data:
        if del_string not in data:
            result_data.append(line)

    print("Для возврата в главное меню, введите цифру '0' ")

def out():
    exit()


if __name__ == "__main__":
    main_menu()

    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 1:
            show_all()
        if choose == 2:
            add_contact()
        if choose == 3:
            find_contact()
        if choose == 4:
            edit_contact()
        if choose == 5:
            del_contact()
        if choose == 6:
            out()
        if choose == 0:
            main_menu()
