# Задача №49. Решение в группах
# Создать телефонный справочник с # возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер # телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в # текстовом файле
# 3. Пользователь может ввести одну из # характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки,
# которую необходимо перенести из одного файла в другой.

from os.path import exists
from csv import DictReader, DictWriter


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
file_2 = 'phone2.csv'


def main():
    info = ["Доступные команды: ",
            "q - завершение программы",
            "r - чтение исходного файла",
            "w - добавление новой записи в исходный файл",
            "c - копирование требуемой записи в отдельный файл"]
    print('\n'.join(' '.join(sl) for sl in info))
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
        elif command == 'c':
            if not exists(file_2):
                print("файл отсутствует, создаем его!")
                create_file(file_2)
                continue
            inf = read_file(file_name)
            n = int(input(f'В файле {len(inf)} строк(-а,-и), введите номер копируемой записи: '))
            buf = [*inf[n - 1].values()]
            write_file(file_2, buf)


main()
