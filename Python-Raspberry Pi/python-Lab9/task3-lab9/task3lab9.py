#  display any key user choose on LCD of gfxhat
from gfxhat import lcd, backlight

def displayObject(obj,x,y):
    backlight.set_all(140,130,250)
    backlight.show()
    for row in range(y,len(obj)+y):
        for column in range(x,len(obj[row-y])+x):
            lcd.set_pixel(column, row, obj[row-y][column-x])
    lcd.show()




def generateDictionary(filename):  
    d = {}
    fileController = open(filename,"r")
    for line in fileController:
        newline=line.split(',')
        key=newline[1][0]
        value=newline[0][2:]
        d[key]=value
    try:
        # get key from user and find in file txt 
        key = input("Enter any Key LCD show >> : ")
        #   each key seprated in 2-digit 
        
        hexdec=d[key]
        d[key]=value
        
        pair_list=[d[key][0:2],
        d[key][2:4],
        d[key][4:6],
        d[key][6:8],
        d[key][8:10],
        d[key][10:12],
        d[key][12:14],
        d[key][14:16]]
        
        dec = int(hexdec, 16)
        hexa= hex(dec)
        binary1=bin(dec)
        
        # show 8*8 list
        font=[list(bin(dec)[0:8]),
        list(bin(dec)[8:16]),
        list(bin(dec)[16:24]),
        list(bin(dec)[24:32]),
        list(bin(dec)[32:40]),
        list(bin(dec)[40:48]),
        list(bin(dec)[48:56]),
        list(bin(dec)[56:len(bin(dec))])]

        
        w="\n".join([ str(i) for i in font if i])
        
        print(key," In file >> ",hexdec,'\n'," In 2-digit >> ",'\n',pair_list,'\n'," In binary >> ",'\n',binary1,'\n'," In 8*8 list >> ",'\n',w)
        
     
        # for i in range(0,len(font)):
        #     font[i]=int(font[i])          # convert string to int
        
        # displayObject(font,64,34)         # display  key on Lcd of gfx       

        
    except:
        print('Unable to find key in this file, Try again !!!!')


generateDictionary("font3.txt")


 






    




