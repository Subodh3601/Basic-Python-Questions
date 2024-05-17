'''
1111
2222
3333
4444

'''


n = int(input("enter the number: "))
i =1
while i<=n:

    j=0
    while j<n:
        print(i,end="")
        j+=1

    print()
    i +=1

'''
1234
1234
1234
1234
'''

n = int(input("enter the number: "))
i =1
while i<=n:

    j=1
    while j<=n:
        print(j,end="")
        j+=1

    print()
    i +=1

'''
4321
4321
4321
4321

'''

n = int(input("enter the number: "))
i =1
while i<=n:

    j=n
    while j>0:
        print(j,end="")
        j-=1

    print()
    i +=1

'''
1
11
202
3003

'''
n = int(input("enter the number: "))
i =1
while i<=n:

    j=1
    while j<=i:
        if i==1:
            print(i,end="")
        elif j!=1 and j!=i:
            print(0,end="")
        else:
            print(i-1,end="") 
        j += 1

    print()
    i +=1

'''
1
11
121
1221
12221

'''
n = int(input("enter the number: "))
i =1
while i<=n:

    j=1
    while j<=i:
        if i==1:
            print(i,end="")
        elif j!=1 and j!=i:
            print(2,end="")
        else:
            print(1,end="") 
        j += 1

    print()
    i +=1

'''
1234
123
12
1

'''

n = int(input("enter the number: "))
i = 0
while i<n:

    j=1
    while j<=n-i:
        print(j,end="") 
        j += 1

    print()
    i +=1