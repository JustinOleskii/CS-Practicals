# Write a program to convert all vowels in a text file from upper to lower case and vice-versa.
f = open('sample.txt', 'r')
o = open('output3.txt', 'a')

content = f.readlines()

for i in content:
    for j in i:
        if j.islower():
            o.write(j.upper())
        elif j.isupper():
            o.write(j.lower())
        else:
            o.write(j)

f.close()
o.close()

o = open('output3.txt', 'r')
oContent = o.readlines()

print("Contents of the file are: ")
for i in oContent:
    print(i)