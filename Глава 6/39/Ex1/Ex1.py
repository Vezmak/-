
import pickle
class TBook:
    pass
Books = []
for i in range(100):
    Books.append(TBook())


B = TBook()
C = TBook()
F = open("books.dat", "wb")
for B in Books:
 B.author = "Trgenew"
 B.title = "Mymy"
 B.count = 2
 C.author = "PuPkin"
 C.title = "Panzerfagen"
 C.count = 14
 pickle.dump(B, F)
F.close()

F = open("books.dat", "rb")
while True:
    try:
        Books.append(pickle.load(F))
    except:
        break
print(B.author, B.title, B.count, sep=", ")
print(C.author, C.title, C.count, sep=", ")
F.close()

N = len(Books)
for i in range(0, N-1):
    for j in range(N-2, i-1, -1):
        if Books[j].author > Books[j+1].author:
            Books[j], Books[j+1] = Books[j+1], Books[j]

