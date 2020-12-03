# Write a program to count total no. of lines beginning with ‘A’ in a text file.
f = open('sample.txt')

content = f.readlines()
counter = 0

for i in content:
    if i[0] == "A":
        counter += 1

print("Total number of lines beginning with 'A': ", counter)
