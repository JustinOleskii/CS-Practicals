# Write a program to read a CSV file and show details of only those students who have even Roll.
# WARNING: POTENTIALLY BROKEN CODE. DO NOT USE.

import csv

f = open('students.csv')
fReader = csv.reader(f)
flag = 0

for row in fReader:
    if row[0] % 2 == 0:
        flag = 1
        print("Details of student are: ", row)
    if flag == 1:
        break
if flag == 0:
    print("Record not found.")
f.close()