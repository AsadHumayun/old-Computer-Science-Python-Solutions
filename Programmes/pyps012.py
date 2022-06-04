'''
Ask for two numbers.  If the first one is larger that the second, display the second number first and then the first number, otherwise show the first number first and then the second. 
'''
def fn(): 
	num = int(input("enter a number: "))
	num1 = int(input("enter a (different) number: "))
	if num > num1:
		print(str(num), str(num1))
	else:
		print(str(num1, str(num)))