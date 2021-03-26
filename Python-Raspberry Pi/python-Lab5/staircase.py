
# staircase(0)
from gfxhat import lcd
from time import sleep
from rokn0001Library import staircase
lcd.clear()
lcd.show()

x = int(input("Input the X Line: "))
y = int(input("Input the Y Line: "))
w = int(input("Input the Width: "))
h = int(input("Input the Height: "))

staircase(x,y,w,h)

sleep(10)
lcd.clear()
lcd.show()
    
