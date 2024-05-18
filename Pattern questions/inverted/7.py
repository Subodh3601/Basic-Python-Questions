'''
*
 * *
  * * *
   * * * *
  * * *
 * *
*
for n = 7
'''
import math
n = int(input('enter the number:'))

i = 1
while i<=math.ceil(n/2):

    m = i-1
    while m > 0:
        print(" ",end="")

        m -= 1

    j = 1
    while j<=i:
        print("* ",end="")

        j += 1



    print()
    i += 1

p = 1
while p<=math.floor(n/2):

    k = math.floor(n/2) - p
    while k > 0:
        print(" ",end="")

        k -= 1

    z = math.floor(n/2)-p+1
    while z>0:
        print("* ",end="")

        z -= 1



    print()
    p += 1
