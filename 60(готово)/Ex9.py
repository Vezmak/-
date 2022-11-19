'''Дружественные числа – это два натуральных числа, таких, что сумма всех делителей одного
числа (меньших самого этого числа) равна другому числу, и наоборот. Найдите все пары
дружественных чисел, каждое из которых меньше 10000. Используйте функцию, которая
вычисляет сумму делителей числа.'''

max = 10000

def sum(n):
    sum = 0
    for k in range(1, n//2+1):
        if n%k == 0:
            sum += k
    return sum
l = [0, 1]
for m in range(2, max + 1):
    l.append(sum(m))
for i in range(2, max + 1):
    for j in range(i + 1, max + 1):
        if i == l[j] and j == l[i]:
            print(i, j)
