from math import pi, sqrt
from gfxhat import lcd, backlight
from random import randint
from time import sleep


def gfxhatClearScreen():
  lcd.clear()
  lcd.show()


# this function has to recive a float number returns a float
# Parameters must be positive and != 0


def calculateAreaOfCircle(radius):
    return (radius ** 2) * pi


# this function has to recive float numbers as parameter returns a float
# Parameters must be positive
def calculateMilesPerGallon(miles, gallons):
    return miles / gallons


# this function has to recive a float number returns a float
def convertTempFToTempC(degreesFahrenheit):
    return (degreesFahrenheit - 32) * 5/9


# this function has to recive 4 int numbers and returns a float
# Parameters must be positive
# x1 must be > x
# x1 must be > y
def calculateDistanceBetweenTwoCoordenates(x, y, x1, y1):
    distanceX = x1-x
    distanceY = y1-y
    return sqrt((distanceX**2)+(distanceY**2))

# this function draw a vertical line in the given position
# Parameter given is x which must be between 0 and 127
def drawVerticalLine(x=64):
  for i in range(0,64):
    lcd.set_pixel(x,i,1)
  lcd.show()


# this function draw a horizontal line in the given position
# Parameter given is y which must be between 0 and 63
def drawHorizontalLine(y=32):
  for i in range(0,128):
    lcd.set_pixel(i,y,1)
  lcd.show()


# this function draw a staircase line in the given direction
# Parameters given are:
# x which must be between 0 and 127
# y which must be between 0 and 63
# width for the staircase
# height for the staircase
# right boolean value for direction of width
# down boolean value for direction of height
def drawStaircase(x,y, width, height, right = True, down = True):
  countX = x
  countY = y
  while((countX<128 and countX>-1) or (countY<64 and countY>-1)):
    countWidth = 1
    countHeight = 1
    while(countWidth<=width):
      lcd.set_pixel(countX, countY, 1)
      if(right):
        countX+=1
      else:
        countX-=1
      countWidth+=1
      if(not (countX<128 and countX>-1) or  not (countY<64 and countY>-1)):
        lcd.show()
        return
    
    while(countHeight<=height):
      lcd.set_pixel(countX, countY, 1)
      if(down):
        countY+=1
      else:
        countY-=1
      countHeight+=1
      if(not (countX<128 and countX>-1) or  not (countY<64 and countY>-1)):
        lcd.show()
        return
  lcd.show()


# Display a random pixel for amount of seconds
# Parameter is the number of seconds the pixel will remain in the screen
def randomPixelsForTime(seconds):
  count = seconds

  while(count>=0):
    lcd.set_pixel(randint(0,127), randint(0,63), 1)
    lcd.show()
    sleep(0.2)
    count -=0.2
  

# reset backlight
def clearBacklight():
  backlight.set_all(0,0,0)
  backlight.show()

# Parameters: 
# obj is a matrix 2D, 
# x is the x coordenate of initial position,
# y is the y coordanate of initial position
def displayObject(obj, x, y):
  objWidth = len(obj[0])
  objHeight = len(obj)

  if(objWidth+x > 127 or x<0):
    raise Exception('Drawing out of screen!')
  if(objHeight+y > 63 or y<0):
    raise Exception('Drawing out of screen!')

  for i in range(y,64):
    for j in range(x,124):
      if((j-x)<objWidth and (i-y)<objHeight):
        lcd.set_pixel(j,i,obj[i-y][j-x])
  lcd.show()