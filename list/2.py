# liner search 
"""
find the given input in list if finds then return index if not then return -1

"""
n = input("enter the space separated list:").split()

m = int(input('enter the number to search:'))
index = []
for i in range(len(n)):
    if m == int(n[i]):
        index.append(i)
        continue
if len(index)>0:
    print(index)
else:
    print(-1)        
    
        