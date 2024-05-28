'''
merging two sorted array

You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third array/list such that the third array is also sorted.


'''

a1 = [2,4,6,8,10]
a2 = [4,5,7,9]
a3 =[]
i=0
j=0
len1 = len(a1)
len2 = len(a2)

while i<len1 and j<len2:
    if a1[i]<a2[j]:
        a3.append(a1[i])
        i += 1
            
    else:  
        a3.append(a2[j])
        j += 1  
while i<len1:
    a3.append(a1[i])
    i += 1
while j<len2:
    a3.append(a2[j])
    j += 1                 


print(a3)            

