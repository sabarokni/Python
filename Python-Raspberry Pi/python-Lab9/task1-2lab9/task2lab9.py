
# a python program that prompts the user for the name of .csv file then reads and displays,
#  each line of the file as a Python list.

import csv


# BoyName as a list 
with open("2000_BoysNames.csv", "r") as f:
    reader = csv.reader(f)
    boy_list = list(reader)
print ("The Boys Names as a List :")
print( boy_list)




# GirlName  as a list 
with open("2000_GirlsNames.csv", "r") as f:
    reader = csv.reader(f)
    girl_list = list(reader)
print ("The Girls Names  as a List : ")
print (girl_list)

