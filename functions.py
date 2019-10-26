import os
import shutil


def display():
    print("""
    Выберите одно из действий: 
    1. создать папку
    2. удалить (файл/папку)
    3. копировать (файл/папку)
    4. просмотр содержимого рабочей директории
    5. посмотреть только папки
    6. посмотреть только файлы
    7. просмотр информации об операционной системе
    8. создатель программы
    9. играть в викторину
    10. мой банковский счет
    11. смена рабочей директории
    12. выход
    """)


def remove_file_or_dir():
    cwd = os.getcwd()
    while True:
        print("""
                Выберите одно из действий: 
                1. удалить папку
                2. удалить файл
                3. вернуться в главное меню
            """)
        choice = input("Выбранное действие: ")
        if choice == '1':
            name_of_dir = input("Введите имя папки: ")
            if name_of_dir in os.listdir(path=cwd):
                shutil.rmtree(name_of_dir)
                print("Папка успешно удалена.")
                break
            else:
                print("В вашей директории нет папки с таким именем.")

        elif choice == '2':
            name_of_file = input("Введите имя файла: ")
            if name_of_file in os.listdir(path=cwd):
                os.remove(name_of_file)
                print("Файл успешно удалён.")
                break
            else:
                print("В вашей директории нет файла с таким именем.")
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')


def copy_file_or_dir():
    cwd = os.getcwd()
    while True:
        print("""
                Выберите одно из действий: 
                1. копировать папку
                2. копировать файл
                3. вернуться в главное меню
            """)
        choice = input("Выбранное действие: ")
        if choice == '1':
            src = input("Введите имя папки-источника: ")
            dst = input("Введите имя папки-приемника: ")
            if src in os.listdir(path=cwd) and dst not in os.listdir(path=cwd):
                shutil.copytree(src, dst)
                print("Папка успешно скопирована.")
                break
            else:
                print("Проверьте отсутствие папки-приемника и существование папки-источника.")
        elif choice == '2':
            src = input("Введите имя файла-источника: ")
            dst = input("Введите имя файла-приемника: ")
            if src in os.listdir(path=cwd):
                shutil.copyfile(src, dst)
                print("Файл успешно скопирован.")
                break
            else:
                print("В вашей директории нет файла с таким именем.")
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')


def print_dirs():
    cwd = os.getcwd()
    onlydirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
    print(onlydirs)


def print_files():
    cwd = os.getcwd()
    onlyfiles = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    print(onlyfiles)


def info_about_creator():
    print("""
    This program was written dy mr.serko, 2019, Moscow, all rights reserved
    """)


def change_dir():
    new_path = input("Введите путь к желаемой директории: ")
    if not os.path.isabs(new_path):
        new_path = os.path.join(r'C:\Users', new_path)
    os.chdir(new_path)