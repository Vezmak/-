"""Напишите программу, которая вводит натуральные числа a и b, и выводит сумму квадратов
натуральных чисел в интервале от a до b."""
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(0)
while a!=b+1:
    c = c + a*a
    a=a+1
print(c)
