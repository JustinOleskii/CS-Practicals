f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')

content = f1.readlines()
for i in content:
    for j in i.split():
        if j.lower() == 'india':
            f2.write("INDIA ")
        else:
            f2.write(j)
            f2.write(" ")

f1.close()
f2.close()
