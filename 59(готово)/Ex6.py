'''Напишите процедуру, которая выводит на экран запись числа, меньшего, чем 216 = 65536, в
виде 4-х знаков в шестнадцатеричной системе счисления.'''


def convert_hex(DEC):
    return hex(DEC)[2::]


print(convert_hex(int(input("Введите число: "))))
