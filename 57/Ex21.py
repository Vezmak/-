"""Напишите программу, которая определяет, верно ли, что введённое число – трёхзначное."""
a = int(input("Введите число: "))

if 100<=a<=999:
    print("Число трехзначное")
else:
    print("Число не трехзначное")