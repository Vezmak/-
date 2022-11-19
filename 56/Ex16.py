"""Напишите программу, которая вводит два целых числа, а и b (a < b), и выводит на экран 5
случайных целых чисел на отрезке [a,b]"""
import random
i=0
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
m=[]
while i<5:
  m.append(random.randint(a,b))
  i=i+1

print(m)