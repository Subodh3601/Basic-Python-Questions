'''
Problem statement
Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.

'''

arr = [2,58,1,0,548,33,22]


i= 0 
while i<=len(arr)-1: 
    minimun = i
    start = i+1
    for j in range(start,len(arr)):
        if arr[minimun] < arr[j]:
            continue
        else:
            minimun = j
    arr[i],arr[minimun]=arr[minimun],arr[i]        
    i += 1

print(arr)

