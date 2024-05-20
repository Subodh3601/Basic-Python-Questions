'''
find palindrome or not

'''
'''
1.for number
'''
n = int(input("enter a number"))

def reverseNum(num):
    original = num
    reverseOfNumber = 0
    while num>0:
     lastDigit = num % 10
     reverseOfNumber = reverseOfNumber * 10 +lastDigit
     num //=10
    print("reverse",reverseOfNumber)
    return reverseOfNumber == original

isPalindrome = reverseNum(n)
print(isPalindrome)   


'''
for string
'''
# n = input("Enter a number: ")
# arr = list(n)

# def revers(x):
#     reverseOfstring = ""
#     while len(x) > 0:
#         lastDigit = x.pop()
#         reverseOfstring += lastDigit
#     print("Reversed:", reverseOfstring)
#     return reverseOfstring

# def palindrome(num):
#     rev = revers(list(num))  # Pass a copy of the list to avoid modifying the original
#     if rev == num:
#         return True
#     else:
#         return False

# isPalindrome = palindrome(n)
# print(isPalindrome)


# '''
# 3. Using String Slicing
# '''
# n = input("Enter a number/string: ")

# def is_palindrome(num):
#     return num == num[::-1]

# is_palindrome_result = is_palindrome(n)
# print(is_palindrome_result)

# '''
# 4.Using a Loop

# '''
# n = input("Enter a number: ")

# def is_palindrome(num):
#     length = len(num)
#     for i in range(length // 2):
#         if num[i] != num[length - i - 1]:
#             return False
#     return True

# is_palindrome_result = is_palindrome(n)
# print(is_palindrome_result)

# '''
# 5: Using Built-in Functions

# '''
# n = input("Enter a number: ")

# def is_palindrome(num):
#     return num == ''.join(reversed(num))

# is_palindrome_result = is_palindrome(n)
# print(is_palindrome_result)
