import pickle
L = []
f1 = open('stu1.txt', 'rb')
f2 = open("stu2.txt", 'wb')

name = " "
flag, c = 0, 0

def bCopy(file_name, list):
    while True:
        try:
            L = pickle.load(file_name)
            name = L[0]
            length = len(name)
            if name[(length-1)] == 'A':
                flag = 1
            if flag == 1:
                print("Record is found!")
                pickle.dump(L, f2)
        except EOFError:
            break
                

while True:
    try:
        L = pickle.load(f1)
        name = L[0]
        if ord(name[0]) >= 65 and ord(name[0] <= 90):
            for i in name:
                if ord(i) >= 97 and ord(i) <= 122:
                    k = 1
                    break
                elif i == " ":
                    k = 1
            if k == 0:
                pickle.dump(L, f2)
                flag = 1
                c += 1
    except EOFError:
        break

if flag == 0:
    print("no such record is found or copied.")
elif flag == 1:
    print(c, " records founds and successfully copied. \n")
    f2.close()
    f3 = open('b2.txt', 'rb')
    size = 0
    print("Contents of the copied file are: ") 

while True:
    try:
        L = pickle.load(f3)
        name = L[0]
        print("name of student is: ",L[0])
        roll = L[1]
        print("roll no of student is: ", L[1])
        print('\n')
        size += 1
    except EOFError:
        break

print("Total no of records:, ", size)
file3.close()

file1.close()