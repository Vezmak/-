"""Напишите программу, которая вводит номер месяца и выводит название времени года. При
вводе неверного номера месяца должно быть выведено сообщение об ошибке."""

a = int(input("Введите номер месяца: "))
if 1<=a<=12:
    match a:
        case 1:
            print("Январь")
        case 2:
             print("Февраль")
        case 3:
             print("Март")
        case 4:
            print("Апрель")
        case 5:
            print("Май")
        case 6:
            print("Июнь")
        case 7:
            print("Июль")
        case 8:
            print("Август")
        case 9:
            print("Сентябрь")
        case 10:
            print("Октябрь")
        case 11:
            print("Ноябрь")
        case 12:
            print("Декабрь")
else:
    print("Такого месяца не существует")