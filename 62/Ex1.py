'''Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов
 нужно ввести с клавиатуры.'''


#first_element = int(input(""))
#raznost = int(input(""))
#Kol_vo_Elementov = int(input(""))

N = int(input("количество элементов"))
P = int(input("первый элемент массива: "))
S = int(input("разность элементов"))
#print(*range(P, P + S * N, S))
A = [*range(P, P + S * N, S) ]

print("Массив:", A)




