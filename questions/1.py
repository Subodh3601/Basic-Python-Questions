# find a prime number if found print -1 if not print all factors side  by side

a = int(input("enter a number"))

isPrime = True

for i in range(2,a):
    if a%i==0:
        print(i,end=" ")
        isPrime=False
    i +=1
if isPrime:
    print(-1)        