'''
   1
  212
 32123
4321234

'''

n = int(input("enter the number:"))

i = 0 

while i<=n:

    j = n-i
    while j>0:
        print(" ",end="")

        j -= 1

    k = i
    while k>0:
        print(k,end="")
        k -= 1

    l = 1
    m = 2
    while l <i:
        print(m,end="")
        l +=1
        m += 1    


    print()
    i += 1