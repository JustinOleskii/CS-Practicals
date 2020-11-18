fileinput = open('input.txt', 'r')
output = open('output.txt', 'w')

content = fileinput.readlines()

for i in content:
    for j in i.split():
        print(j, end='?')