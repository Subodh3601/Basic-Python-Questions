
'''
Problem statement
You are given an integer array 'arr' of size 'N'.



You must sort this array using 'Insertion Sort' recursively.

'''
# arr = [120,1,25,11,140,22,2,0]

# for i in range(1,len(arr)):
#     j=i-1
#     while j>=0:
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

#         j -= 1    

# print(arr)

'''
other
'''
arr = [120,1,25,11,140,22,2,0]

for i in range(1,len(arr)):
    j=i-1
    temp = arr[i]
    while j>=0 and arr[j]>temp:
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = temp       

print(arr)



