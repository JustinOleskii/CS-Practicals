# Write a menu driven program to Push and Pop an integer element in an List-Stack.
def Push(stack, item):
    stack.append(item)
    top = len(stack) - 1

def Pop(stack):
    if isEmpty(stack):
        return "Underflow"
    else:
        item = stack.pop()
        if len(stack) == 0:
            top = None
        else:
            top = len(stack) - 1
    return item

def Peek(stack):
    if isEmpty(stack):
        return "Underflow"
    else:
        top = len(stack) - 1
        return stack[top]

def Display(stack):
    if isEmpty(stack):
        return "Underflow"
    else:
        top = len(stack) - 1
        print(stack[top], "<= top")
        for i in range(top-1, -1, -1):
            print(stack[i])

def isEmpty(stack):
    if Stack == []:
        return True
    else:
        return False

Stack = []
top = None

while True:
    print("Stack Operations")
    print("1. Push\n2. Pop\n3. Peek\n4. Display Stack\n5. Exit\n\n")
    c = int(input("Enter your choice: "))
    if c == 1:
        item = int(input("Enter item: "))
        Push(Stack, item)
    elif c == 2:
        item = Pop(Stack)
        if item == "Underflow":
            print("Underflow. Stack is empty.")
        else:
            print("Popped item is: ", item)
    elif c == 3:
        item = Peek(Stack)
        if item == "Underflow":
            print("Underflow! Stack is empty.")
        else:
            print("Topmost item is: ", item)
    elif c == 4:
        Display(Stack)
    elif c == 5:
        break
    else:
        print("Invalid choice!")