"""Напишите программу, которая вводит трёхзначное число и разбивает его на цифры. например, при вводе числа 123 программа должна вывести «1, 2, 57»."""
a = int(input("Введите трехзначное число: "))
print(a//100, (a%100)//10, a%10)