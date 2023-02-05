
def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)

def get_search_name() -> str:
    return input("Введите фамилию для поиска: ")

def get_search_prof() -> str:
    return input("Введите профессию для поиска: ")

def get_search_salary() -> int:
    return int(input("Введите зарплату для поиска: "))

def get_new_user() -> str:
    id = ("Введите идентификатор записи")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    profession = input("Введите профессию: ")
    salary = input("Введите зарплату: ")
    return f'{id},{last_name},{first_name},{profession},{salary}'


def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")
