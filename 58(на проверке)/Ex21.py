"""Напишите программу, которая вводит с клавиатуры числа до тех пор, пока не будет введено
число 0. В конце работы программы на экран выводится сумма и произведение введенных
чисел (не считая 0)"""

a=int(input("Введите число: "))
b=a
sum=0
proiz=1

while a!=0:
    a = int(input("Введите число: "))
    sum+=a
    if a!=0:
        proiz=proiz*a


print("Сумма введенных чисел: ", sum+b)
print("Произведение введенных чисел: ", proiz*b)