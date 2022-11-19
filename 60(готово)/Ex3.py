'''Напишите функцию, которая вычисляет наибольший общий делитель двух чисел.'''
# import math
# a = int(input(" ")); b = int(input(" "))
# print(math.gcd(a, b))

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = int(input("А = "))
b = int(input("B = "))

print("NOD =", gcd(a, b))
