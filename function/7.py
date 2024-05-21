'''
Create a function that determines whether a given number N belongs to the Fibonacci sequence. If N is found in the Fibonacci sequence, the function should return true; otherwise, it should return false.

'''
n = int(input("enter the number:"))

firstNum = 0
secNum = 1

add = 0
arr = [0,1]
while add<= n:

    add = firstNum + secNum
    firstNum = secNum
    secNum = add
    arr.append(add)

if n in arr:
    print("True")
else:
    print("False")        