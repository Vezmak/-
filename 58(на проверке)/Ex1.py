"""Напишите программу, которая вводит два целых числа и находит их произведение,
не используя операцию умножения. Учтите,
что числа могут быть отрицательными."""

n = int(input("Введите число1: "))
m = int(input("Введите число2: "))
while m>2:
    n=n+n
    m=m-1
print(n)