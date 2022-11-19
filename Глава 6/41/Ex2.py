'''Напишите программу, которая вычисляет значение арифметического
выражения, записанного в постфиксной форме. Выражение вводится с
клавиатуры в виде символьной строки. Предусмотрите сообщения об ошибках.'''

data = input().split()
st = []

for x in data:
 if x in "+-*/":
     op2 = int(st.pop())
     op1 = int(st.pop())
     if x == "+": res = op1 + op2
     elif x == "-": res = op1 - op2
     elif x == "*": res = op1 * op2
     else: res = op1 // op2
     st.append (res)
 else:
    st.append(x)

if x not in "+-*/":
    print("Error")
elif len(x) != 1:
    print("Лишний знак")
else:
    print(st[0])