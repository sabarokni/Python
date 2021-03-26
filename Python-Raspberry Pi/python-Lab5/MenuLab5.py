# Menu of Lab 5
from rokn0001Library import vertical_line,horizontal_line,staircase,Random_Pixel,backlight_clear_reset
from gfxhat import lcd
from time import sleep
def Menu():
 choice = '0'
 while choice != 6:
    print("************MAIN MENU**************")
    sleep(1)
    print("\nWelcome to Python Lab 5!\n")
    sleep(1)
    print("\nPlease enter a number for what you want to do.\n")
    print("Enter 1 for a vertical line.")
    print("Enter 2 for a horizontal line.")
    print("Enter 3 for a staircase.")
    print("Enter 4 for a random pixel.")
    print("Enter 5 for backlight clear and reset.")
    print("Enter 6 to quit.\n")
    choice = int(input("Please make a choice: "))
    if choice == 1:
      x1 = int(input("Input the X Line: "))
      vertical_line(x1)

    elif choice ==2:
      y1 = int(input("Input the Y Line: "))
      horizontal_line(y1)
      
    elif choice==3:
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

    elif choice==4:
      lcd.clear()
      lcd.show()
      Random_Pixel(5)
      sleep(10)
      lcd.clear()
      lcd.show()

    elif choice==5:
      backlight_clear_reset()
    else:
       exit()
      
Menu()

