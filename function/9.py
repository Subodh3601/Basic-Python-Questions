'''
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

'''


def printTable(start,end,step):
#Implement Your Code Here

	for i in range(start,end+1,step):
		celsius = (5/9)*(i-32)
		print(i," ",int(celsius))

	pass 

	   
s = int(input("enter start:"))
e = int(input("enter end:"))
step = int(input("enter step:"))
printTable(s,e,step)





