"""Напишите программу, которая вводит с клавиатуры 10 чисел и вычисляет их сумму и произведение."""
a=0
sum=0
proiz=1

for i in range(1,11):
    a=int(input("Введите число: "))
    sum+=a
    proiz*=a

print("Сумма введенных чисел: ", sum)
print("Произведение введенных чисел: ", proiz)
