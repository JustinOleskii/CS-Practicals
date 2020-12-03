# Consider a binary file “Emp.dat” containing details such as empId , ename and salary .Write a program to display details of those employees whose salary is between 20000 and 40000.
import pickle
f = open('Emp.dat')
flag = False
while True:
    try:
        rec = pickle.load(f)
        if rec['salary'] >= 20000 and rec['salary'] <= 40000:
            print("Employee name: ", rec['ename'])
            print("Employee ID: ", rec['empId'])
            print("Employee salary: ", rec['salary'])
            flag = True
    except EOFError:
        break
if flag == False:
        print("No records found.")
f.close()

