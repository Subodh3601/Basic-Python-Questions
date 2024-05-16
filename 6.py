# print binary of decimal number


# n = int(input("enter the number : "))
# binRep = ""
# if n == 0:
#     binRep = "0"
# while n>0:
#     if n%2==0:
#         binRep = "0"+binRep
#     else:
#         binRep = "1" + binRep

#     n //= 2
# print("binary of decimal number is:", binRep)            


# binary to decimal 

n = int(input("enter the binary:"))
dec = 0
pow_of_two = 1 #2**0

while n>0:
   # extract the last digit
   lastDigit = n%10
   dec += lastDigit*pow_of_two
   pow_of_two *= 2
   #remove the last degit so that next digit can be multiplied by pow of 2
   n //=10
print("decimal of binary is:",dec)   
      
 
