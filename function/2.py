# prime number using function

def isPrime(num):
    prime = True
    for i in range (2,num):
        if num%i == 0 :
            prime = False
    return prime        


n = int(input("input number:"))

m = isPrime(n)
if(m):
    print("number is prime")
else:
    print("number is not prime")    