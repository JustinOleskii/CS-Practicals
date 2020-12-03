import csv
f = open('students.csv', 'w')
fWriter = csv.writer(f)

fWriter.writerow(['Roll No.', 'Name', 'Class', 'Marks'])
size = int(input("Enter number of records to create: "))

for i in range(1, size+1, 1):
    roll = int(input("Enter roll no.: "))
    name = input("Enter name: ")
    sclass = int(input("Enter class: "))
    marks = int(input("Enter marks: "))
    fWriter.writerow([roll, name, sclass, marks])
f.close()

o = open("students.csv", 'r')
fReader = csv.reader(o)
for row in fReader:
    print(row)
o.close()
