'''Напишите процедуру, которая принимает параметр – натуральное число N – и выводит первые N чисел Фибоначчи (см. задания к § 58(на проверке). ).'''


def fib(N):
    a = b = 1
    i = 0
    while i < N:
        i += 1
        s = a + b
        a = b
        b = s
        print(s)
fib(10)
