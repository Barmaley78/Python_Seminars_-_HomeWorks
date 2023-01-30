
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


# def view_data(data, title):
#     print(f'{title} = {data}')

def read_csv(file_name):
    employee = []
    data = open(file_name, 'r', encoding="utf-8")
    lst = data.read()
    for row in lst:
        temp = {}
        temp["id"] = row[0]
        temp["last_name"] = row[1]
        temp["first_name"] = row[2]
        temp["position"] = row[3]
        temp["phone_number"] = row[4]
        temp["salary"] = float(row[5])
        employee.append(temp)
    data.close()
    return employee


def write_csv(file_name, lst):
    data = open(file_name, 'w')
    data.write(lst)
    data.close()
    return
