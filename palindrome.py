fileInput = open('input.txt', 'r')
output = open('output.txt', 'w')

content = fileInput.readlines()
c = 0
for i in content:
    for j in i.split():
        if j == j[::-1]:
            c += 1

print("The number of palindromes are: ", c)