'''
for input 4

*000*000*
0*00*00*0
00*0*0*00
000***000

'''

n = int(input('enter the number:'))

i = 1

while i<=n:
    
    
    p = 1
    while p <i:
        print("0",end="")
        p += 1

    print("*",end="")

    secondZeros = n-i
    while secondZeros > 0:
        print("0",end="")

        secondZeros -= 1    

    print("*",end="")

    secZeros = n-i
    while secZeros > 0:
        print("0",end="")

        secZeros -= 1 

    print("*",end="")    

    m = 1
    while m <i:
        print("0",end="")
        m += 1   

    print()
    i += 1