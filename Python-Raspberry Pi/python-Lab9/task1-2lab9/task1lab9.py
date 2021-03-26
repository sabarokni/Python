# You must write a python program that reads each text file then converts it into a csv format: "name",
# count then saves the entry in a csv file. The output csv file must 
# include the following header as its first line: "First Name","Count"
import csv;


       
# text file then converts it into a csv format Boys name txt file
with open('2000_BoysNames.txt', 'r') as in_file:
    strip1 = (row.strip() for row in in_file)
    rows = (row.replace(" ",",").split()for row in strip1)
    with open('2000_BoysNames.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('First Name', 'Count'))
        writer.writerows(rows)

f1=open("2000_BoysNames.csv","r")
reader1 = csv.reader(f1)
next(reader1,None)
print("Boys Name : ")
#row is a list of all elements in the csv line
for rows in reader1:
    for el in rows:
        print(el)


       
# text file then converts it into a csv format Girls name txt file
with open('2000_GirlsNames.txt', 'r') as in_file:
    strip1 = (row.strip() for row in in_file)
    rows = (row.replace(" ",",").split()for row in strip1)
    with open('2000_GirlsNames.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('First Name', 'Count'))
        writer.writerows(rows)    

f2=open("2000_GirlsNames.csv","r")
reader2 = csv.reader(f2)
next(reader2,None)
print("Girls Name : ")
#row is a list of all elements in the csv line
for row in reader2:
    for e in row:
        print(e)