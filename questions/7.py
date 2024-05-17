# nested loop
# print the first 20 number multiplication table from 1 to 10

n = int(input("enter the number to till which table to print:"))

for value in range(1,n+1):
    for i in range(1,11):
        print(value*i," ", end="")
    print()

