# Write a program to read a text file and count total no. of lower case vowels in it.
f = open('sample.txt', 'r')

content = f.readlines()
counter = 0
for i in content:
    for j in i:
        if j == "a" or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            counter += 1

print("Total number of lower case vowels: ", counter)