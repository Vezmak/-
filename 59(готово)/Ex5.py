"""Напишите процедуру, которая выводит на экран запись числа, меньшего, чем 8^10, в виде 10
знаков в восьмеричной системе счисления."""

def conv_oct(DEC):
    return oct(DEC)[2::]
print (conv_oct(int(input("Введите число: "))))