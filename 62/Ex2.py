''' Заполните массив степенями числа 2 (от 2^1до 2^N).'''


n = int(input("Степень до которой будет идти счёт: "))

A = [2**i for i in range(1, n+1)]

print("Массив:", A)

