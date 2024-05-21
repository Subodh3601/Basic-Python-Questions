'''
factorial of a number

'''
n = int(input('enter a number:'))

fact = 1
while n>=1:
    fact = fact*n
    n = n-1
print("factorial is:",fact)     

   