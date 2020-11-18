def upperCheck(D):
    for key in D:
        if key.isupper():
            print("Name: ", key, " Roll No.:", D[key])

students = {}
n = int(input("How many details would you like to input?\n"))
for i in range(0, n):
    key = input("Enter name: ")
    value = input("Enter roll: ")
    students[key] = value

upperCheck(students)
