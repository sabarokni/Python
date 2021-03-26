from gfxhat import lcd,backlight
from click import getchar
from random import randrange

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayObject(obj,x,y):
    backlight.set_all(240,230,200)
    backlight.show()
    for row in range(y,len(obj)+y):
        for column in range(x,len(obj[row-y])+x):
            lcd.set_pixel(column, row, obj[row-y][column-x])
    lcd.show()

def eraseObject(obj,x,y):
    for row in range(y,len(obj)+y):
        for column in range(x,len(obj[row-y])+x):
            lcd.set_pixel(column, row, 0)
    lcd.show()
    
def moveObject(obj,x,y,vx,vy):
    eraseObject(obj, x, y)
    x=x+vx
    y=y+vy
    displayObject(obj, x, y)
    print(x)
    return (x,y)
    # for row in range(y,len(obj)+y):
    #     for column in range(x,len(obj[row-y])+x):
    #         lcd.set_pixel(column, row, obj[row-y][column-x])
    #         lcd.show()

def checkCollision(obj,x,y,vx,vy,Sx=128,Sy=64):
    # eraseObject(obj, x, y)
    if(x<0):
        x=x+vx
    elif(y<0):
        y=y+vy
    elif(y>63+len(obj)):
        y=y-vy
    elif(x>127 and x=len(obj[row-y])):
        x=x-vx
    # displayObject(obj,x,y)
    return(x,y)

        
# x= int(input("The X :"))
# y= int(input("The Y :"))
x=64
y=55
vx=-1
vy=-1
while(True):
    key = getchar()
    if (key == 'b'):
        ball =  [
        [0,0,0,1,1,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,1,1,0,0,0]
        ]
        lcd.clear()
        lcd.show()    
        displayObject(ball, x, y)
    if (key == 'a'):
        ball =  [
        [0,0,0,1,1,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,1,1,0,0,0]
        ]
        lcd.clear()
        lcd.show()
        while(True):
            print(x)
            x,y = moveObject(ball, x, y, vx, vy) 
    if(key=='e'):
        lcd.show() 
        eraseObject(ball,x,y)

    if (key=='q'):
        backlight.set_all(0, 0, 0)
        backlight.show()
        lcd.clear()
        lcd.show()
        break