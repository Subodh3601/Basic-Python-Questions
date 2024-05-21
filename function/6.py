'''
prime and composite

'''

# n = int(input("enter a number"))

# def isPrime(num):
#     i=2
#     prime = True
#     while i<num:
#         if num%i == 0:
#             prime = False
#         i+=1
#     print("number is prime or not:",prime)

# isPrime(n)    

'''
composite upto the given number
'''
n = int(input("enter a number"))

def isComposite(num):
    j=4
    while j<=num:
        i=2
        prime = True
        while i<j:
            if j%i == 0:
                prime = False
                break
            i+=1
        if not prime:
            print(j) 
        j+=1

isComposite(n)