# Write a program to display those only those words which begin with ‘a’ or ‘A’ in a string.

def process(inputStr):
    newstr = ""
    for word in inputStr.split(" "):
        if word[0] == 'A' or word[0] == 'a':
            newstr += "{} ".format(word)
    
    return newstr

L = []
L = input("Enter your string: ")
print(process(L))

