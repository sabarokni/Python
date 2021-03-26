from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

backlight.set_all(255,255,255)
backlight.show()

displayText('etch a sketch',lcd,20,20)

x=64
y=63

while(True):
  keyOfKeyboard = getchar()
  if(keyOfKeyboard == 's'):
    clearScreen(lcd)
  if(keyOfKeyboard == 'q'):
    clearScreen(lcd)
    backlight.set_all(0,0,0)
    backlight.show()
    exit()
  if(keyOfKeyboard == '\x1b[A'):
    y-=1
  if(keyOfKeyboard == '\x1b[B'):
    y+=1
  if(keyOfKeyboard == '\x1b[C'):
    x+=1
  if(keyOfKeyboard == '\x1b[D'):
    x-=1

  if(x>127):
    x=0
  elif(x<0):
    x=127
  
  if(y>63):
    y=0
  elif(y<0):
    y=63
  
  lcd.set_pixel(x,y,1)
  lcd.show()
