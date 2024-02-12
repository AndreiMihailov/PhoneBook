# 55. Создать телефонный справочник с возможностью
# импорта и экспорта данных в формате .txt
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле

# 1. Программа должна выводить  данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь можжет ввести одну из характеристик
#    для поиска определённой записи
# 4. использование функций. Программа не должна быть линейной

import os

def check_file_exists(filename):
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write("")

def add_new_user (name: str, phone: str, filename: str):
    """
    Добавляет новую запись в телефонную книгу
    :param name:
    :param phone:
    :param filename:
    :return:
    """
    with open(filename, 'r+t', encoding = 'utf-8') as data:
        lines_count = len(data.readlines())
        data.write(f"{lines_count + 1};{name};{phone}\n")

def read_all(filename: str) -> str:
    """
    Возвращает всё содержимое телефонной книги
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding = 'utf-8') as data:
        result = data.read()
    return result

def search_user(data, filename):
    """
    Поиск записи по критерию data
    :param data:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        result = [item for item in text if data.lower() in item.lower()]
    return (''.join(result)).replace(';', ' ') if result else "Входений не найдено"

def copy_record(number: str, filename_source: str, filename_dest: str):
    """
    Ищет запись по заданному номеру
    и копирует ее в заданный новый файл

    :param number: требуемый номер строки
    :param filename_source:  имя исходного файла, в котором ищется запись
    :param filename_dest:  имя файла, в который копируется запись
    :return: отсутсвует
    """
    check_file_exists(filename_dest) # Проверяем наличие файла и при его отсутствии создаём новый
    with open(filename_source, 'r', encoding='utf-8') as source:
        with open(filename_dest, 'a', encoding='utf-8') as dest:
            text = source.readlines()
            result = [item for item in text if number in item]
            if result:
                dest.write(result[0])
            else:
                print("Строка с заданным номером во входном файле отсутсвует")

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск записи
4 - копирование записи
"""

DATA_SOURCE = "phone.txt"

check_file_exists(DATA_SOURCE)
while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATA_SOURCE))
    elif mode == 2:
        user = input("Введите имя ")
        phone = input("Введите номер телефона ")
        add_new_user(user, phone, DATA_SOURCE)
    elif mode == 3:
        search = input("Введите строку для поиска")
        print(search_user(search, DATA_SOURCE))
    elif mode == 4:
        number = input("Введите номер копируемой записи")
        name = input("Введите имя результирующего файла")
        copy_record(number, DATA_SOURCE, name)
