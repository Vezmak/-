'''Напишите программу, которая «переворачивает» массив,
записанный в файл, с помощью стека. Размер массива неизвестен'''

F = open("input.txt")
st = []
while True:
    s = F.readline()
    if not s: break
    st.append(int(s))
F.close()

F = open("output.txt", "w")
while len(st) > 0:
    x = st.pop()
    F.write(str(x)+"\n")
F.close()

