# Write a program to read a file and count total no. of words 'am' in it.
f = open('sample.txt')
content = f.readlines()
counter = 0

for i in content:
    for j in i.split():
        if j == 'am':
            counter += 1

print("Total occurences of 'am' are: ", counter)
