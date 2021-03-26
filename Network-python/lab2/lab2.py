import os,shutil
os.mkdir('cst8254')
os.mkdir('cst8254/linux')
os.mkdir('cst8254/backup')
os.mkdir('cst8254/python')
os.mkdir('cst8254/linux/labs')
os.mkdir('cst8254/linux/lectuers')
os.mkdir('cst8254/linux/labs/Lab1')
os.mkdir('cst8254/linux/labs/Lab2')
os.mkdir('cst8254/linux/labs/Lab3')
os.mkdir('cst8254/linux/lectuers/Week1')
os.mkdir('cst8254/linux/lectuers/Week2')
os.mkdir('cst8254/linux/lectuers/Week3')

f = open("lab3-1.txt", "x")
os.system('cp lab3-1.txt lab3-2.txt')
# shutil.copy2(destination, source)
os.system('mv lab3-1.txt cst8254/linux/labs/Lab3')
os.system('cp lab3-2.txt cst8254/linux/labs/Lab3')

print("it worked")


