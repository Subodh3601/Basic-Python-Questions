# reverse the digits of a number

# OPTION=1
n = int(input("enter number with digits>1  :  "))

while n>0:
    a = n%10
    print(a,end="")
    n = n//10

# OPTION=2
n = input("enter number with digits>1  :  ")
newArray = []

for digit in n :
    newArray.append(int(digit))

newArray.reverse()

reversed_string = ''.join(map(str, newArray))

print(reversed_string)


'''map(str, newArray):

The map function applies a given function to all items in an input list (or any iterable) and returns an iterator.
Here, map is used to apply the str function to each item in newArray.
newArray is a list of integers, and map(str, newArray) converts each integer in newArray to its string representation.
For example, if newArray = [5, 4, 3, 2, 1], the result of map(str, newArray) would be an iterator that produces the sequence '5', '4', '3', '2', '1'.

''.join(...):

The join method is a string method that concatenates the elements of an iterable (in this case, the string representations of the numbers) into a single string, with a specified separator.
'' (an empty string) is used as the separator, meaning there will be no characters inserted between the elements being joined.
Essentially, ''.join(...) concatenates all the elements of the iterable into a single string.
Continuing with the example, if the elements are '5', '4', '3', '2', '1', then ''.join(...) concatenates them into the string '54321'.'''