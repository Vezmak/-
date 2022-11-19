'''В предыдущей задаче выведите все найденные слова в файл
 в порядке убывания частоты, то есть в начале списка должны стоять слова,
 которые встречаются в файле чаще всех.'''

D = {}
F = open("test.txt")
while True:
    word = F.readline().strip()
    if not word: break
    D[word] = D.get(word, 0) + 1
F.close()

F = open("p1test.txt", "w")
for k in sorted(D.keys(), key=D.get, reverse=True):
    F.write("{}: {}\n".format(k, D[k]))
F.close()

for k in sorted(D, key=D.get, reverse=True):
 print(k, "->", D[k])
