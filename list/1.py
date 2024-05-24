'''
Given an array of length N, you need to find and print the sum of all elements of the array.

Sample Input :
3
9 8 9
Sample Output :
26
'''
# n = (input("enter the number:")).split()
# total = 0
# for i in n:
#     total = total + int(i)

# print("total: ",total)    

n = int(input("enter the number:"))
items = input("enter the space seperated values:").split()
# print(items[1])
arr = []
total = 0
for i in range(n):
    arr.append(int(items[i]))

for ele in arr:
    total += ele
print("total: ",total)