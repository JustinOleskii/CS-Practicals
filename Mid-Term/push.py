stack = []
top = 0

def Push(stackObj, item):
    stackObj.append(item)

item = int(input("Enter item: "))
Push(stack, item)