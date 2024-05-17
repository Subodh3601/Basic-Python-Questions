'''
ABCD
ABCD
ABCD
ABCD

'''

# n = int(input('enter the number of row:'))

# i = 1

# while i<=n:

#     j = 1
#     while j<=n:
#         charP = chr(ord("A")+j-1)
#         print(charP, end="")
#         j += 1


#     print()
#     i += 1

'''
ABCD
BCDE
CDEF
DEFG

'''

# n = int(input('enter the number of row:'))

# i = 1

# while i<=n:

#     j = 1
#     p = i
#     while j<=n:
#         charP = chr(ord("A")+p-1)
#         print(charP, end="")
#         p +=1
#         j += 1


#     print()
#     i += 1

'''
A
BC
CDE
DEFG

'''
# n = int(input('enter the number of row:'))

# i = 1

# while i<=n:

#     j = 1
#     p = i
#     while j<=i:
#         charP = chr(ord("A")+p-1)
#         print(charP, end="")
#         p +=1
#         j += 1


#     print()
#     i += 1

'''
print the pattern equal to row number entered and 
alphabet shoul start from that entered number

if N = 5

E
DE
CDE
BCDE
ABCDE


'''
n = int(input('enter the number of row:'))

i = 1
startingChar = chr(65+n)
while i<=n:

    j = 1
    while j<=i:
        charP = chr(ord(startingChar)-i+j-1)
        print(charP, end="")
        j += 1


    print()
    i += 1