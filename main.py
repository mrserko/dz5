import os
import platform
import functions
from victory import victory
from bank_account import account, exit

while True:
    functions.display()
    choice = input('Выберите пункт меню')
    if choice == '1':
        name_of_dir = input("Введите имя папки: ")
        os.mkdir(name_of_dir)
    elif choice == '2':
        functions.remove_file_or_dir()
    elif choice == '3':
        functions.copy_file_or_dir()
    elif choice == '4':
        cwd = os.getcwd()
        print(os.listdir(path=cwd))
    elif choice == '5':
        functions.print_dirs()
    elif choice == '6':
        functions.print_files()
    elif choice == '7':
        print(platform.uname())
    elif choice == '8':
        functions.info_about_creator()
    elif choice == '9':
        victory()
    elif choice == '10':
        account()
    elif choice == '11':
        functions.change_dir()
    elif choice == '12':
        exit()
        break
    else:
        print('Неверный пункт меню')