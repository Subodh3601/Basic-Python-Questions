''''
shifting the element to its prevoius index
'''

n = int(input("enter the number of list:"))

for i in range(n):
    m = int(input(f"enter the number of element in list {i+1}: "))
    items = input("enter the numbers:").split()
    for j in range(m-1):
        items[j],items[j+1]= items[j+1],items[j]

print(items)