# Write a program to count the number of time 'MCS' appears in a file

fileinput = open('input.txt', 'r')
data = fileinput.readlines()
c = 0

for i in data:
    for j in i.split():
        if j == "MCS":
            c += 1
print(c)