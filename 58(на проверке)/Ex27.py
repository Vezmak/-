""" Напишите программу, которая вводит натуральные числа a и b и выводит все простые числа
в диапазоне от a до b. """

a = int(input("Введите  число а: "))
b = int(input("Введите  число b: "))

for number in range(a, b + 1):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                break
        else:
            print(number)
