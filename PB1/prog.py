f = open('old.txt', 'r')
f2 = open('new.txt', 'w')
contents = f.readline()

for i in contents:
    if i == 0:
        f2.write(contents[i].capitalize())
    elif contents[i] == ' ' and contents[i - 1] == '.':
        f2.write(contents[i + 1])
    else:
        f2.write(contents[i])

 