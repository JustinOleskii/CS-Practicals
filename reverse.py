output = open('output.txt', 'w')
fileInput = open('input.txt', 'r')

data = fileInput.read()
newContent = data[::-1]

output.write(newContent)
output.close()
