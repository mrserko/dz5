import random
borndays = {
    "А.С.Пушкин" : ["06.06.1799", "шестое июня 1999 года"],
    "А.П.Гайдар" : ["22.01.1904", "двадцать второе января 1904 года"],
    "Л.Н.Толстой" : ["09.09.1928", "девятое сентября 1928 года"],
    "М.Ю.Лермотнов" : ["15.10.1814", "пятнадцатое октября 1814 года"],
    "Джон Леннон" : ["09.10.1940", "девятое октября 1940 года"],
    "Эми Уайнхаус" : ["14.09.1983", "четырнадцатое сентября 1983 года"],
    "Дэвид Ли Рот" : ["10.10.1954", "десятое октября 1954 года"],
    "Пол Маккартни" : ["16.06.1942", "шестнадцатое июня 1942 года"],
    "Винсент Ван Гог" : ["30.03.1853", "тридцатое марта 1853 года"],
    "Пабло Пикассо" : ["25.10.1881", "двадцать пятое октября 1881 года"],
}


def victory():
    try_again = None
    while try_again != "н":
        persons_to_ask = random.sample(borndays.keys(), 5)
        right_answers = 0

        for i in range(5):
            person = persons_to_ask[i]
            print("Когда родился ", person, "? (В формтае (дд.мм.гггг.)")
            answer = input("Ваш ответ:")
            if answer == borndays[person][0]:
                right_answers += 1
            else:
                print("Неверно! Правильный ответ: ",  borndays[person][1])
        print("Правильных ответов:", right_answers)
        print("Неправильных ответов:", 5 - right_answers)

        try_again = None
        while try_again != "д" and try_again != "н":
            try_again = input("Хотите попробовать ещё раз (д/н)? ")
    print("Спасибо за игру!")