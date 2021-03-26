import math


def Area_Of_Circle(r):

    a = math.pi*r**2
    return a


def Fahrenheit_To_Celsius(f):
    c = (f-32)*5.00/9.00
    return c


def MPG(m, g):

    mpg = float(m/g)
    return mpg

# a function that displays a vertical line at a given x coordinate on the gfx hat
def vertical_line(x):
    from gfxhat import lcd
    from time import sleep
    lcd.clear()
    lcd.show()
    for y in range(0,64):
        lcd.set_pixel(x,y,1)
        lcd.show()
    sleep(6)
    lcd.clear()
    lcd.show()
   


