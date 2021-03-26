import socket
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw
import time

def getMyIp():
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 myIp = s.getsockname()[0]
 s.close()
 return myIp

def displayIpOnGFX():
	led_states = [False for _ in range(6)]
	width, height = lcd.dimensions()
	image = Image.new('P', (width, height))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype(fonts.AmaticSCBold, 22)
	text =  getMyIp()

	w, h = font.getsize(text)
	x = (width - w) // 2
	y = (height - h) // 2

	draw.text((x, y), text, 1, font)

	backlight.set_all(120,120,120)

	backlight.show()

	for x in range(128):
    		for y in range(64):
        		pixel = image.getpixel((x, y))
        		lcd.set_pixel(x, y, pixel)

	lcd.show()
	time.sleep(10)
#	input('< Hit a key >')
	lcd.clear()
	lcd.show()
	backlight.set_all(0,0,0)
	backlight.show()

displayIpOnGFX()
