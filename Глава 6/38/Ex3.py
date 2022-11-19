'''Без использования программы определите,
 сколько нулей стоит в конце числа 100!'''

from math import factorial as fac

n = fac(100)

a = 0

while n % 10 == 0:
    a += 1
    n //= 10
print(a)
