def read_csv(filename: str) -> list:
    data = []
    fields = ["Id","Фамилия", "Имя", "Профессия", "Зарплата"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_json(filename: str, data: list):  #поменять на json кодировку
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return list(el.values())
    return "Такой абонент отсутвует"

def find_by_prof(data: list, prof: str) -> str:
    for el in data:
        if el.get("Профессия") == prof:
            return list(el.values())
    return "Такой абонент отсутвует"

def find_by_salary(data: list, sal: int) -> str:
    for el in data:
        if el.get("Зарплата") == sal:
            return list(el.values())
    return "Такой абонент отсутвует"

def add_user(data: list, user_data: str):
    fields = ["Id","Фамилия", "Имя", "Профессия", "Зарплата"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)