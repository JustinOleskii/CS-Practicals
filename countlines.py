# Write a program to count total no. of lines in a program which have three words:
f=open("myfile.txt", 'r')
c,c1=0,0
for i in f:
    T=len(i)
    c=0
    for j in range(0,T,1):
        if i[j]=='':
            c=c+1
    if c==2:
        c1=c1+1
        print(i)
print("number of lines with 3 words: ",c1)
f.close()