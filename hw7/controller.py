from view import (menu, print_result, get_search_name,
                  get_search_number, get_new_user, get_file_name)
from model import write_txt, write_csv, read_csv, find_by_name, find_by_number, add_user

def work_with_phonebook():
    choice = menu()
    phone_book = read_csv('phonebook.csv')


    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 3:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 4:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 2:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = menu()