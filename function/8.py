'''
Given two numbers, x, and y, calculate and Return their GCD.

GCD stands for "Greatest Common Divisor." It refers to the largest positive integer that divides two or more numbers without leaving a remainder. 

'''

num1 = int(input("input number 1:"))
num2 = int(input("enter number 2:"))

def find_GCD(num1,num2):
    arr =[]
    i=2
    while i<=min(abs(num1),abs(num2)):
        if num1%i==0 and num2%i==0:
            arr.append(i)
        i+=1  
    if len(arr)>0:    
        maxnumber = max(arr)  
    else:
        maxnumber = 1       
    return maxnumber
    
    
    
print(find_GCD(num1, num2))

# another approach

num1 = int(input("input number 1: "))
num2 = int(input("enter number 2: "))

def find_GCD(num1, num2):
    x = max(num1, num2)
    y = min(num1, num2)

    # Handle case when one of the numbers is zero
    if y == 0:
        return 1
    

    while y > 0:
        old_y = y
        y = x % y
        x = old_y
        print("X", x, "Y", y)
    return x

print(find_GCD(num1, num2))
