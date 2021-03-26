import csv

f=open("airports.csv","r")
reader = csv.reader(f)
next(reader,None)

#row is a list of all elements in the csv line
for row in reader:
    for el in row:
        print(el)
