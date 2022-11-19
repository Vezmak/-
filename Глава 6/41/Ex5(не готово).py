'''Напишите вариант предыдущей программы,
в котором в качестве стека используется символьная строка.'''

L = "([{<"
R = ")]}>"

stack = []
err = False

s = input("Введите скобочки: ")

for c in s:
    p = str(R.find(c))
    if c in L:
        stack.append(c)
    p = int(R.find(c))
    if p >= 0:
        if not stack: err = True
        else:
            top = stack.pop()
            if p != L.find(top):
                err = True
    if err: break

if len(stack) > 0: err = True
if not err:
    print("Выражение правильное")
else:
    print("Выражние не правильное")