str = input("Введите строку, которую надо перевернуть: ")
str_reverse = ""
for letter in str:
    str_reverse = letter + str_reverse
print(str_reverse)