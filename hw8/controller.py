from view import (show_menu, get_search_name,
                  get_search_prof, get_search_salary, get_new_user, get_file_name)
from model import (write_json, write_csv, read_csv, find_by_name, 
                   find_by_prof, find_by_salary, add_user)

def work_with_db():
    choice = show_menu()
    db = read_csv('db.csv')


    while (choice != 9):
        if choice == 1:
            name = get_search_name()
            print(find_by_name(db, name))
        elif choice == 2:
            prof = get_search_prof()
            print(find_by_prof(db, prof))
        elif choice == 3:
            sal = get_search_salary()
            print(find_by_salary(db, sal))
        elif choice == 4:
            user_data = get_new_user()
            add_user(db, user_data)
            write_csv('db.csv', db)
        elif choice == 5:
            pass # удалить сотрудника
        elif choice == 6:
            pass # обновить данные сотрудника
        elif choice == 7:
            file_name = get_file_name()
            write_json(file_name, db)
        elif choice == 8:
            file_name = get_file_name()
            write_csv(file_name, db)
        choice = show_menu()