from gfxhat import lcd,backlight

def eraseObject(obj,x=0,y=0):
    lcd.clear()
    lcd.show()

while(True):
    key = getchar()
    if(key=='e'):
        e=[0]
        lcd.clear()
        lcd.show() 
        eraseObject(e,0,0)

