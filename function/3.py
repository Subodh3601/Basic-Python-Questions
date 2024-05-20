'''
find palindrome or not

'''
'''
1.for number
'''
n = int(input("enter a number"))

def reverseNum(num):
    reverseOfNumber = 0
    while num>0:
     lastDigit = num % 10
     reverseOfNumber = reverseOfNumber * 10 +lastDigit
     num //=10
    print("reverse",reverseOfNumber)
    return reverseOfNumber

def palindrome(num):
   rev = reverseNum(num)

   if rev == num:
      return True
   else:
      return False
isPalindrome = palindrome(n)
print(isPalindrome)   


'''
for string
'''
n = input("Enter a number: ")
arr = list(n)

def revers(x):
    reverseOfstring = ""
    while len(x) > 0:
        lastDigit = x.pop()
        reverseOfstring += lastDigit
    print("Reversed:", reverseOfstring)
    return reverseOfstring

def palindrome(num):
    rev = revers(list(num))  # Pass a copy of the list to avoid modifying the original
    if rev == num:
        return True
    else:
        return False

isPalindrome = palindrome(n)
print(isPalindrome)
