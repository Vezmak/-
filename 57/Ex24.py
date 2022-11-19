"""Напишите программу, которая вводит с клавиатуры номер месяца и день, и определяет,
сколько дней осталось до Нового года. При вводе неверных данных должно быть выведено
сообщение об ошибке."""
from datetime import datetime
from calendar import monthrange
i=0
count = 0
month = int(input("Введите номер месяца: "))
day = int(input("Введите номер дня: "))
current_year = datetime.now().year
days1 = monthrange(current_year, month)[1]
while(i<month):
    days = monthrange(current_year, month)[1]
    count = count+days
    i=i+1
print("Количество дней до нового года: ", 365-(count-(days1-day)))

