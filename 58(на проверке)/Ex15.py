""" Напишите программу,
которая определяет, верно ли, что введённое число состоит из
одинаковых цифр (как, например, 222)."""

a = str(input("Введите число: "))
flag = bool(True)

for i in range(len(a)-1):
    if a[i]==a[i+1]:
        flag=flag&True
    else:
        flag=flag&False
if flag==True:
    print("Число состоит из одинаковых цифр")
else:
    print("Число состоит из разных цифр")


