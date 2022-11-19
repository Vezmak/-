'''Дополните предыдущую программу так, чтобы
она определяла номер ошибочного символа в строке.'''

L = "([{<"
R = ")]}>"

stack = []
err = False

s = "()(()"      #input("Введите скобочки: ")
n = 0
for c in s:
    n += 1
   # p = str(R.find(c))
    if c in L:
        stack.append(c)
    p = int(R.find(c))
    if p >= 0:
        if not stack: err = True
        else:

            top = stack.pop()
            if p != L.find(top):
                err = True
    if err:break

if len(stack) > 0: err = True
if not err:
    print("Выражение правильное")
else:
    print("Выражние не правильное", n)