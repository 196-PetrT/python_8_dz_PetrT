# Задача №49. Решение в группах
# Создать телефонный справочник с # возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер # телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в # текстовом файле
# 3. Пользователь может ввести одну из # характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа # не должна быть линейной


from os.path import exists
from csv import DictReader, DictWriter


# class LenNumberError(Exception):
#     def __init__(self, txt):
#         self.txt = txt

def get_info():
    first_name = "Иван"
    second_name = "Петров"
    phone_number = "89992223311"

    return [first_name, second_name, phone_number]


def create_file(file_name):
    # with - менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        # fieldnames - шапка таблицы
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        # делает запись заголовка
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("файл отсутствует, создайте его!")
                continue
            print(read_file(file_name))

main()





