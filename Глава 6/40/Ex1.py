'''Постройте полную программу, которая составляет
алфавитно-частотный словарь для заданного файла со списком слов'''

D = {}
F = open("test.txt")
while True:
    word = F.readline().strip()
    if not word: break
    D[word] = D.get(word, 0) + 1
F.close()

allKeys = D.keys()
sortKeys = sorted(D.keys())

F = open("ptest.txt", "w")
for k in sorted(D.keys()):
    F.write("{}: {}\n".format(k, D[k]))
F.close()

for k, v in D.items():
 print ( k, "->", v )

