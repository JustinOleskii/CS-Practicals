# Write a program to swap every element which is multiple of 7 with the next element in a tuple

def swap(T):
    L = []
    for i in T:
        temp = 0
        if i % 7 != 0:
            L.append(i)
        else:
            temp = i
            L.append(i+1)
            L.append(temp)

    return tuple(L)

T = (1, 14, 3, 7, 2)
print(swap(T))