'''. Опишите структуру, в которой хранится информация о
а) видеозаписи;
б) сотруднике фирмы «Рога и Копыта»;
в) самолёте;
г) породистой собаке.'''
import pickle
class Video:
    pass
class employee:
    pass
class Airplane:
    pass
class Pesik:
    pass

Infa = []


V = Video()
E = employee()
A = Airplane()
P = Pesik()
F = open("Infa.dat", "wb")
V.raz = int(360)
V.dlit = "40 минут"
pickle.dump(V, F)
E.fam = "Лопаткин И.Л"
E.zarp = int(15300)
pickle.dump(E, F)
A.kolvo = int(162)
A.dist = 1500, "km"
pickle.dump(A, F)
P.mlevel = "прикольный"
P.poroda = "Двортерьер"
pickle.dump(P, F)
F.close()
F = open("Infa.dat", "rb")
while True:
    try:
        Infa.append(pickle.load(F))
    except:
        break
print(V.dlit, V.raz)
print(E.fam, E.zarp)
print(A.kolvo, A.dist)
print(P.poroda, P.mlevel)
F.close()

