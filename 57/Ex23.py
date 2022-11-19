"""Напишите программу, которая вводит с клавиатуры номер месяца и определяет, сколько
дней в этом месяце. При вводе неверного номера месяца должно быть выведено сообщение об ошибке."""
from datetime import datetime
from calendar import monthrange

current_year = datetime.now().year
month = int(input("Введите номер месяца: "))
if 1<=month<=12:
    days = monthrange(current_year, month)[1]
    print(days)
else:
    print("Такого месяца не существует")


