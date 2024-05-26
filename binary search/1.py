'''
Problem statement
You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'.



Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.



Note:

You must write an algorithm whose time complexity is O(LogN)

'''
import math

n =int(input("enter the number: "))
m = int(input("inter the number to search :"))
arr = []
for i in range(0,n):
    arr.append(int(input(f"enter the number {i} : ")))
arr.sort()
lower = 0
upper = len(arr)-1

index = 0
while lower<=upper:
    middle =math.floor((lower+upper)/2)
    if arr[middle] == m:
        index = middle
        break
    elif arr[middle] > m :
        upper = middle -1
        
    else:
        lower = middle +1 

if index == 0:
    print("not found : ",-1)
    
else:
    print("index of number : ",index)      


