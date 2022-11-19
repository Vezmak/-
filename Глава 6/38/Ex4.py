'''Соберите всю программу и вычислите 100!. Сколько цифр входит в это число?'''
from math import factorial as fac

n = str(fac(100))
print("Само число:",n)

c = len(n)
print(c)




