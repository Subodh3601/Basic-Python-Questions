'''Problem statement
You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.

You don't need to print or return anything, just change in the input array itself.

Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4
Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2 :
3 9 12 6 32 4 11 5 19 
2 1 4 3 
'''

n = int(input("enter the number of list:"))

for i in range(n):
    m = int(input(f"enter the number of element in list {i+1}: "))
    items = input("enter the numbers:").split()
    for j in range(0,m-1,2):
        items[j],items[j+1]= items[j+1],items[j]

print(items)