"""
Now that you have learnt how to perform Binary Search, let us try
writing code for another edge case. Suppose your sorted array has
duplicate numbers.
For example, if the array is as follows: [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
Try writing the code for the following two cases.
1. Finding first occurrence of the given number.
2. Finding the last occurrence of the given number.

"""

def find_first_occurrence(array, element, debug=False):
    lower_bound = 0
    upper_bound = len(array) - 1
    first_occurrence = -1
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if debug:
            print("Lower Bound", lower_bound)
            print("Upper Bound", upper_bound)
            print("Middle", middle)
        if element == array[middle]:
            first_occurrence = middle
            upper_bound = middle - 1  # Continue searching in the left half
        elif element < array[middle]:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return first_occurrence

def find_last_occurrence(array, element, debug=False):
    lower_bound = 0
    upper_bound = len(array) - 1
    last_occurrence = -1
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if debug:
            print("Lower Bound", lower_bound)
            print("Upper Bound", upper_bound)
            print("Middle", middle)
        if element == array[middle]:
            last_occurrence = middle
            lower_bound = middle + 1  # Continue searching in the right half
        elif element < array[middle]:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return last_occurrence

# Test the functions
array = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
element = 3

first_index = find_first_occurrence(array, element)
last_index = find_last_occurrence(array, element)

if first_index == -1:
    print("First occurrence: number not found")
else:
    print(f"First occurrence of number {element} is at index {first_index}")

if last_index == -1:
    print("Last occurrence: number not found")
else:
    print(f"Last occurrence of number {element} is at index {last_index}")
