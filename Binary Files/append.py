#  Write a program to append data in a binary file and show all the data values on the screen.
import pickle
D = {}
f = open('data.dat', 'ab')

n = int(input("Enter number of records: "))

for i in range(1, n+1, 1):
    name = input("Enter name of book: ")
    bID = int(input("Enter book ID: "))
    D[name] = bID
    pickle.dump(D, f)

f.close()