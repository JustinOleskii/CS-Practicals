# Write a program to read a file line by line and display each word separated by a ‘#'.
f = open('sample.txt')
content = f.readlines()

for i in content:
    for j in i.split():
        print(j, end="#")