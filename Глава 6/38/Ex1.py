'''Докажите, что если у числа k
нет ни одного делителя в в диапазоне от 2 до k
, то оно простое.'''
from math import sqrt as sq

n = int(input(""))
A = [True]*(n+1)

k = 2

for k in range(2, int(sq(n))+1):
    if A[k]:
        for i in range(k*k, n, k):
            A[i] = False
P = [i for i in range(2,n+1) if A[i]]
print(P)


