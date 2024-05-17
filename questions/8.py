'''Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the requiredSum and computing the product of all integers in the range 1 to N (both inclusive).



If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)'''

n= int(input("enter the number: "))
c = int(input("enter the choice=> 1 means SUM and 2 means product: "))
# requiredSum

if c==1:
    requiredSum = 0
    for i in range(n,0,-1):
        requiredSum += i
    print("result as per choice: ",requiredSum)    
elif c==2:
    requiredSum = 1
    for i in range(n,0,-1):
        requiredSum *= i  
    print("result as per choice: ",requiredSum)    
else:
    print("chice entered does not match the requirements:",-1)               
       
       
'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.'''

x = int(input("enter the number: ")) 
n = int(input("enter the power : "))

x, n = input().split()
x =int(x)
n= int(n)

print("power : ", x**n)


'''Problem statement
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.'''

n = int(input("enter the terms you want to print: "))
i=1
count = 0

while count<n:
    if (3*i+2)%4 !=0:  
        print(3*i+2,end=" ")
        count +=1
    i +=1    
        
'''
Problem statement
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Hint : Use type casting'''        

n = int(input("enter the start value:"))
t = int(input("enter the stop value: "))
s = int(input("enter the step :"))

for i in range(n,t+s,s):
    print("celsius of ferenhite:",i," ",int((5/9*(i-32))),end=" ")
    print()


'''Problem statement
Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).

Print the prime numbers in different lines.'''

n = int(input("enter the number:"))

for i in range(2,n+1):
    isPrime = True
    for j in range(2,i):
        if i%j==0:
            isPrime = False
            continue
    if isPrime:
        print("number is prime:", i)        
