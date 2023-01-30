import controller
import view
menu = controller.show_menu()
if menu == 1:
    phone_book = view.read_csv('phonebook.csv')
    print(phone_book)
