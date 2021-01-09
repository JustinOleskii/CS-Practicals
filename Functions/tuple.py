# Write a program to swap every element which is multiple of 7 with the next element in a tuple

T = ()
T = eval(input("Enter elements of tuple: "))
L = list(T)
Z = L[len(T) - 2]

for i in range(0, len(L) - 1, 1):
    if T[i] % 7 == 0:
        L[i], L[i+1] = L[i+1], L[i]
        i += 1

if L[len(L) - 1]%7 == 0 and L[len(L) - 1] != Z:
    L[0],L[len(L)-1]=L[len(L)-1],L[0]
    T = tuple(L)
    print("New tuple:\n ", T)
