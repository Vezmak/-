"""Напишите программу, которая считает количество чётных цифр введённого числа."""

a = int(input("Введите число: "))

n=int(1)
c=0
for i in range(a):
    n+=1
    if n%2 :
        c += 1

print("Чётных чисел всего:", c)