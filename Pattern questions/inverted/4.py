'''
1      1
12    21
123  321
12344321

'''
n = int(input("enter the number:"))

i= 1

while i<=n:

    j = 1
    while j<=i:
        print(j,end="")
        j += 1

    spaces = n-i
    while spaces>0:
        print(" ",end="")
        spaces -= 1  

    

    newSpaces = n-i
    while newSpaces>0:
        print(" ",end="")
        newSpaces -= 1     


    p = 1
    k = i
    while p<=i:
        print(k,end="")
        p += 1
        k -= 1

    print()
    i += 1
