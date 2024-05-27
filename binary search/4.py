'''
Problem statement
You are given an integer array 'arr' of size 'N'.



You must sort this array using 'Bubble Sort'.

'''
# arr = [1,54,2,333,95,64,0,78,895,1000,12]
# i = 0
# while i<len(arr):
#     for m in range(len(arr)):
#         for j in range(i,len(arr)-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr [j+1],arr[j]
#     i += 1
     

# print(arr)

'''
better way
'''

# arr = [1,54,2,333,95,64,0,78,895,1000,12]

# for m in range(len(arr)):
#     for j in range(i,len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr [j+1],arr[j]

    

# print(arr)

'''
opimized version
'''
arr = [1,54,2,333,95,64,0,78,895,1000,12]

for m in range(len(arr)-1):
    for j in range(len(arr)-1-m):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr [j+1],arr[j]

    

print(arr)
