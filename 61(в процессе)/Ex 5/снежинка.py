'''*Используя графические возможности вашего языка программирования,
постройте на экране треугольник Серпинского и другие фракталы.'''
# снежинка

import turtle as tu


def sneg(leng):
    if leng <= 2:
        tu.fd(leng)
        return
    sneg(leng / 3)
    tu.lt(60)
    sneg(leng / 3)
    tu.rt(120)
    sneg(leng / 3)
    tu.lt(60)
    sneg(leng / 3)


tu.speed(0)
length = 500.0
tu.penup()
tu.backward(length / 2.0)
tu.pendown()
sneg(length)
tu.done()
