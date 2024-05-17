#reverse the number but trailing zero should not be present

n = int(input("enter the number : "))
n_str = str(n)
reversed_str = n_str[::-1]

reversed_number = int(reversed_str)

# Print the reversed number
print(reversed_number)

'''expression n_str[::-1] is a Python string slicing technique used to reverse a string. Let's break down how it works:

String Slicing [start:end:step]
In Python, you can use slicing notation on strings to extract substrings or manipulate the order of characters. The syntax [start:end:step] is used for slicing:

start: Starting index of the slice (inclusive). If omitted, it defaults to the beginning of the string (0).
end: Ending index of the slice (exclusive). If omitted, it defaults to the end of the string.
step: Step or stride of the slice. It determines how the indices increase between the start and end values. If omitted, it defaults to 1.

Reversing a String with Slicing
To reverse a string using slicing, you can use a step value of -1. Here's how it works:

[::-1]: This slicing notation specifies:
start: Not specified, defaults to the beginning of the string (0).
end: Not specified, defaults to the end of the string.
step: -1, which means the slice will start from the end of the string and move towards the beginning, effectively reversing the string.
'''