"""Напишите программу, которая строит последовательность из N случайных чисел на отрезке
от 0 до 1 и определяет, сколько из них попадает на отрезки [0; 0,25), [0,25; 0,5), [0,5; 0,75) и
[0,75; 1). Сравните результаты, полученные при N = 10, 100, 1000, 10000."""
import random

N = int(input("Введите число N: "))
numbers=[]
for i in range(20):
    numbers.append(random.random())
print("%.3f"%(numbers))



