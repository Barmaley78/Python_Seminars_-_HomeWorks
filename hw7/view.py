def menu():
    print('Выбирите пункт меню')
    print('1. Вывести справочник')
    print('2. Добавить запись в справочник')
    print('3. Найти абонента по фамилии')
    print('4. Найти абонента по телефону')
    print('5. Сохранить справочник')
    print('6. Выйти')
    key = int(input())
    return key

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)


def get_search_name() -> str:
    return input("Введите фамилию для поиска: ")


def get_search_number() -> str:
    return input("Введите номер телефона для поиска: ")


def get_new_user() -> str:
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    description = input("Введите описание абонента: ")
    phone_number = input("Введите номер телефона: ")
    return f'{last_name},{first_name},{description}б{phone_number}'

def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")