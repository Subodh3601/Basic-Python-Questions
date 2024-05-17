'''
4444
333
22
1

'''
# n = int(input("enter the number: "))

# i=0

# while i<n:

#     j=n-i
#     p=n-i
#     while j>0:

#         print(p,end="")
#         # p += 1
#         j -= 1

#     print()
#     i+=1

'''
Mirror image

    *
   **
  ***
 ****   
'''

# n = int(input("enter the number: "))

# i=0

# while i<n:
#     spaces = 0

#     while spaces <= n-i:
#         print(" ",end="")
#         spaces += 1

#     stars = 0

#     while stars<=i:
#         print("*",end="")
#         stars += 1    

#     print()
#     i+=1

'''
   1
  12
 123
1234

'''

n = int(input("enter the number: "))

i=1

while i<=n:
    spaces = 1

    while spaces <= n-i:
        print(" ",end="")
        spaces += 1

    stars = 1

    while stars<=i:
        print(stars,end="")
        stars += 1    

    print()
    i+=1