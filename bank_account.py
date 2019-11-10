"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import json
history = {}


def display():
    return """
    Меню: 
    1. пополнить счет
    2. покупка
    3. история покупок
    4. выход 
    """


def add_money_to_account(account):
    sum = int(input("Введите сумму, которую Вы хотите добавить к счету."))
    account += sum
    print("На Вашем счету:", account)
    return account


def buy(account):
    sum = input("Введите сумму предполагаемой покупки: ")
    if sum.isdigit():
        sum = int(sum)
    else:
        print("Сумма покупки - это число")
        return account
    if sum > account:
        print("На Вашем счете недостаточно средств.")
        print("На Вашем счету:", account)
        return account
    purchase = input("Введите название покупки: ")
    history[purchase] = sum
    account = account - sum
    print("На Вашем счету:", account)
    return account


def print_history():
    for k, v, in history.items():
        print(k, "-->", v)


def exit_f(account):
    with open("account.txt", 'w') as f:
        json.dump(account, f)
    with open("history_of_purchases.txt", 'w') as f:
        json.dump(history, f)
    print("Спасибо за пользование нашими услугами!")


def account_f():
    if os.path.exists("account.txt"):
        with open("account.txt", 'r') as f:
            account = json.load(f)
    else:
        account = 0
    if os.path.exists("history_of_purchases.txt"):
        with open("history_of_purchases.txt", 'r') as f:
            history = json.load(f)
    while True:
        print(display())
        choice = input('Выберите пункт меню')
        if choice == '1':
            account = add_money_to_account(account)
        elif choice == '2':
            account = buy(account)
        elif choice == '3':
            print_history()
        elif choice == '4':
            exit_f(account)
            break
        else:
            print('Неверный пункт меню')