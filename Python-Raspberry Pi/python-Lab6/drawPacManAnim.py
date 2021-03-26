from gfxhat import lcd, backlight
from time import sleep
from click import getchar
from paes0001Library import displayObject

backlight.set_all(0,255,0)
backlight.show()


pm = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,0,0,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

pm2 = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]


pm3 = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,0,0],
[1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

pm4 = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,0,0,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]


while(True):
  displayObject(pm, 64, 32)
  sleep(.3)
  displayObject(pm2, 64, 32)
  sleep(.1)
  displayObject(pm3, 64, 32)
  sleep(.1)
  displayObject(pm4, 64, 32)
  sleep(.3)
  displayObject(pm3, 64, 32)
  sleep(.1)
  displayObject(pm2, 64, 32)
  sleep(.1)