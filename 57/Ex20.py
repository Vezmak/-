"""Напишите программу, которая выбирает максимальное и минимальное из пяти введённых
чисел (не используя встроенные функции min и max)."""
list = []

for counter in range(5):
  list.append(int(input()))

min = list[1]
max = min

for counter in range(5):
    if list[counter] < min:
            min = list[counter]
    if list[counter] > max:
            max = list[counter]

print(min, max)









