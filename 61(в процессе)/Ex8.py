'''*Напишите рекурсивную процедуру для
 перевода числа в троичную уравновешенную систему счисления.
  Вместо цифры 1 используйте символ «#».'''

def f(n, b):
    if n < b:
        print(n, end='')
    else:
        f(n // b, b)
        print(n % b, end='')

с = int(input(""))
f(123, с)
