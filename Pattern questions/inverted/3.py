'''
   1   
  121   
 12321
1234321 

'''
# n = int(input("enter the number: "))

# i=1

# while i<=n:
#     spaces = 1

#     while spaces <= n-i:
#         print(" ",end="")
#         spaces += 1

#     stars = 1

#     while stars<=i:
#         print(stars,end="")
#         stars += 1  

#     reverseStar = i-1
#     while reverseStar>0:
#         print(reverseStar,end="")
#         reverseStar -= 1    
   

#     print()
#     i+=1

'''
   *
  ***
 *****
*******

'''
# n = int(input("enter the number: "))

# i=1

# while i<=n:
#     spaces = 1

#     while spaces <= n-i:
#         print(" ",end="")
#         spaces += 1

#     stars = 1

#     while stars<=i:
#         print("*",end="")
#         stars += 1  

#     reverseStar = i-1
#     while reverseStar>0:
#         print("*",end="")
#         reverseStar -= 1      

#     print()
#     i+=1

'''
   1
  232
 34543
4567654

'''
# with while loop

# n = int(input("enter the number: "))

# i=1

# while i<=n:
#     spaces = 1

#     while spaces <= n-i:
#         print(" ",end="")
#         spaces += 1

#     stars = i

#     while stars<2*i:
#         print(stars,end="")
#         stars += 1  

#     reverseStar = 2*i-2
#     while reverseStar>i-1:
#         print(reverseStar,end="")
#         reverseStar -= 1      

#     print()
#     i += 1

# for loop

# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     # Print leading spaces
#     print(" " * (n - i), end="")
    
#     # Print increasing numbers
#     for j in range(i, 2*i):
#         print(j, end="")
    
#     # Print decreasing numbers
#     for j in range(2*i - 2, i - 1, -1):
#         print(j, end="")
    
#     # Move to the next line
#     print()

'''
  *
 ***
*****
 ***
  *

'''
import math

n = int(input("enter the number: "))

j=1
while j<= math.ceil(n/2):
    spaces = 1

    while spaces <= (math.ceil(n/2)-j):
        
        print(" ",end="")
        spaces += 1

    stars = 1

    while stars<=j:
        print("*",end="")
        stars += 1  

    reverseStar = j-1
    while reverseStar>0:
        print("*",end="")
        reverseStar -= 1  

    
    j +=1  
    print()  

k=1
while k<= math.floor(n/2):
    spaces = 1

    while spaces<=k:
        
        print(" ",end="")
        spaces += 1

    stars = math.ceil(n/2)-k

    while stars>0:
        print("*",end="")
        stars -= 1  

    reverseStar = math.floor(n/2)-k
    while reverseStar>0:
        print("*",end="")
        reverseStar -= 1  

    
    k +=1  
    print() 

    