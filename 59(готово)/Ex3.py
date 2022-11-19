"""Напишите процедуру, которая выводит на экран все делители переданного ей числа (в одну
строчку)."""

# join нам в параграфе не показывали
# print(" ".join(str(a) for a in range(1, (N>>1)+1) if not(N%a)))
def deliteli(N):
    for a in range(1, (N >> 1) + 1):
        if not (N % a):
            print(str(a), end=" ")


deliteli(100)
