"""Напишите программу, которая вводит возраст человека (целое число, не превышающее 120)
и выводит этот возраст со словом «год», «года» или «лет». Например, «21 год», «22 года»,
«25 лет»."""

age = int(input("Введите возраст: "))
a = int(age%10)
if 0<=age<=99:
    match a:
        case 7:
            print(age, " лет")
        case 8:
            print(age," лет")
        case 9:
            print(age, " лет")
        case 0:
            print(age, " лет")
        case 6:
            print(age, " лет")
        case 5:
            print(age," лет")
        case 1:
            print(age, " год")
        case 4:
            print(age, " года")
        case 3:
            print(age, " года")
        case 2:
            print(age, " года")
else:
    print("Не то число")

