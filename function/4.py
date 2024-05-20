'''
armstrong number

'''
"""
number is not interable so to find the length of number different methods

def length_of_number(num):
    # Method 1: Using string conversion
    length_str = len(str(num))
    
    # Method 2: Using a loop
    length_loop = 0
    temp = abs(num)
    while temp > 0:
        temp //= 10
        length_loop += 1
    if num == 0:
        length_loop = 1

    # Method 3: Using logarithms
    if num == 0:
        length_log = 1
    else:
        length_log = math.floor(math.log10(abs(num))) + 1

    return length_str, length_loop, length_log

num = int(input("Enter a number: "))
lengths = length_of_number(num)
print("Length using string conversion:", lengths[0])
print("Length using loop:", lengths[1])
print("Length using logarithms:", lengths[2])


"""

n = int(input('enter a number:'))

length = int(len(str(abs(n))))

def arm(num):
    original =num
    addition = 0
    while num>0:
        digit = num % 10
        addition = addition + digit**length
        num //=10
    return addition == original

isArmstrong = arm(n)
print(isArmstrong)    
