# fabonacci series

a = int(input("enter the number till fabonacci needed : "))
i=0
s1 = 0
s2 = 1

print(s1,s2,end=" ")
while i<a:
    
    s3 = s1+s2
    s1 = s2
    s2 = s3
    
    print(s3,end=" ")


    i +=1

# Now print the nth bebonacci number ex = if user enter 5 then print only 5th term of febonacci series

n = int(input('enter the nth term to print : '))

firstTerm = 1
secondTerm = 1
i=3
fabonacci = [1,1]
while  i<=n:

    sum = firstTerm + secondTerm
    fabonacci.append(sum)
    firstTerm = secondTerm
    secondTerm = sum   
    i += 1

print("nth term of series : ", fabonacci[n-1])
