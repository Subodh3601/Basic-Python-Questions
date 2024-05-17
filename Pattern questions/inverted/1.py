'''

****
***
**
*

'''

n = int(input("enter the number: "))

i=0

while i<n:

    j=n-i
    while j>0:

        print("*",end="")
        j -= 1

    print()
    i+=1

'''
1234
123
12
1

'''
n = int(input("enter the number: "))

i=0

while i<n:

    j=n-i
    p=1
    while j>0:

        print(p,end="")
        p += 1
        j -= 1

    print()
    i+=1

"""
4321
321
21
1

"""

n = int(input("enter the number: "))

i=0

while i<n:

    j=n-i
    # p=n-i
    while j>0:

        print(j,end="")
        # p += 1
        j -= 1

    print()
    i+=1

'''
1234
567
89
10

'''    
n = int(input("enter the number: "))

i=0
p=1
while i<n:

    j=n-i
    
    while j>0:

        print(p,end="")
        p += 1
        j -= 1

    print()
    i+=1