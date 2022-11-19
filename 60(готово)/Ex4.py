'''Напишите функцию, которая вычисляет наименьшее общее кратное двух чисел.'''

def cal(a, b):
    if a > b:
        c = a
    else:
        c = b
    while(True):
        if((c % a == 0) and (c % b == 0)):
            l = c
            break
        c += 1
    return l
n1 = int(input("A ="))
n2 = int(input("B ="))
print(cal(n1, n2))