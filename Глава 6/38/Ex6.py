'''Напишите процедуры для сложения и вычитания длинных
чисел (не используя «длинную арифметику» Python).'''

def summa(s1, s2):
    p = 0
    l1 = len(s1)
    l2 = len(s2)
    i1 = l1 - 1
    i2 = l2 - 1
    res = ""
    while(True):
        if ((i1<0) and (i2 < 0)):
            break
        if (i1<0):
            a2 = int(s2[i2])+p
            p = a2//10
            a2 = a2%10
            res = str(a2) + res
            i2 -= 1
            if (i2 < 0):
                break
        if (i2 < 0):
            a1 = int(s1[i1]) + p
            p = a1//10
            a1 = a1%10
            res = str(a1) + res
            i1 -= 1
            if (i1 < 0):
                break
        a1 = int(s1[i1])
        a2 = int(s2[i2])
        r = a1 + a2 + p
        p = r//10
        r = r%10
        res = str(r) + res
        i1 -= 1
        i2 -= 1
    if (p > 0):
        res = str(p) + res
    return res
def razn(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if (l1 == l2):
        if s1[0] > s2[0]:
            sgn = 1
            a1 = s1
            a2 = s2
        else:
            sgn = -1
            a1 = s2
            a2 = s1
    else:
        if (l1 > l2):
            sgn = 1
            a1 = s1
            a2 = s2
        else:
            sgn = -1
            a1 = s2
            a2 = s1

    l1 = len(a1)
    l2 = len(a2)
    i1 = l1 - 1
    i2 = l2 - 1
    res = ""
    b = 0
    while (True):
        if ((i1 < 0) & (i2 < 0)):
            break
        if (i1 < 0):
            q2 = int(a2[i2]) - b
            p = q2 // 10
            q2 = a2 % 10
            res = str(q2) + res
            i2 -= 1
            if (i2 < 0):
                break
        q1 = int(a1[i1])
        q2 = int(a2[i2])
        q = q1 - b - q2
        if (q >= 0):
            res = str(q) + res
            b = 0
        else:
            q += 10
            b = 1
            res = str(q) + res
        i1 -= 1
        i2 -= 1

    if (sgn == -1):
        res = "-" + res
    return res


s1 = input("")
s2 = input("")
r = summa(s1, s2)
k = razn(s1, s2)
print("Сумма:", r)
print("Разность:", k)





