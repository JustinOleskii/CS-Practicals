# Write a menu driven program to write the details of n students in a binary file and display details of a particular student on the screen depending on the Roll.
import sys
import pickle
c = 0

print("1. Enter details of Students\n2. Display Details\n\n")
c = int(input("Enter your choice: "))

if c == 1:
    f = open('students.dat', 'ab')
    D = {}
    size = int(input("Enter number of records to enter: "))
    for i in range(1, size+1, 1):
        name = input("Enter name: ")
        roll = int(input("Enter roll no.: "))
        AdmNo = int(input("Enter admission number: "))
        D = {'Name':name, 'Roll Number':roll, 'Admission No.':AdmNo}
        pickle.dump(D, f)
    f.close()
    rF = open('students.dat', 'rb')
    while True:
        try:
            rec = pickle.load(rF)
            print('Name: ', rec['Name'])
            print('Roll Number: ', rec['Roll Number'])
            print('Admission No.', rec['Admission No.'])
        except EOFError:
            break
    f.close()
elif c == 2:
    f = open('students.dat', 'rb')
    flag = False
    roll = int(input("Enter roll no. to search: "))
    while True:
        try:
            rec = pickle.load(f)
            if rec['Roll Number'] == roll:
                print('Name: ', rec['Name'])
                print('Roll Number: ', rec['Roll Number'])
                print('Admission No.: ', rec['Admission No.'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print("No records found.")
    f.close()
else:
    print("Invalid choice. Program exiting!\n")
    sys.exit()
    