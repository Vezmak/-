"""Напишите программу, которая случайным образом выбирает дежурных:
выводит два различных случайных числа в диапазоне от 1 до N,
 где N – количество учеников вашего класса."""

import random

n = int(input("Введите количество учеников: "))
m=[]
i=0
while(i<2):
    m.append(random.randint(1,n))
    i=i+1

print(m)