output = open('output.txt', 'w')
fileInput = open('practical.txt', 'r')

data = fileInput.read()
newC = data[::-1]

output.write(newC)
output.close()
fileInput.close()