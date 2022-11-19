a = 26
b = 6
c = (int(a % b + b))
print("a%b+b =",c)
c = (int(a // b + a))
print("a // b + a = ",c)
b = (int(a // b))
c = a // b
print("a // b = ",c)
b = (int(a // b + b))
c =(int(a % b + a))
print("a % b + a = ",c)
b = int(a % b + 4)
c = int(a % b + 1)
print("c = a % b + 1 = ",c)
b = int(a // b)
c = int(a % (b + 1))
print("b = a // b\n   a % (b + 1)=", c)
b = int(a % b)
c = int(a // (b + 1))
print("b = a % b\n   a // (b + 1) = ", c)




