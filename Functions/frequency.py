# Write a program to display frequency of all elements of a list.

def frequency(inputList):
    freq = {}
    for i in inputList:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        print("{} : {}".format(key, value))

L = [1, 1, 1, 1, 5, 6, 3, 2, 5, 6]
frequency(L)
