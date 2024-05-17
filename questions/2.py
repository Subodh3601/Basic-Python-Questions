# reverse of a number series

a = input("enter the number series seperated by comma")

Array = a.split(',') 
print(Array)
numberArray = []
for i in Array:
    numberArray.append(int(i))   # shorter way = number_array = [int(element) for element in string_array]
numberArray.reverse()
print(numberArray)