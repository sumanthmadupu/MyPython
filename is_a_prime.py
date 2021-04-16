#Takes a number as an input and will tell whether it is a prime number or not

def is_a_prime(inp):
	for i in range(2,int(inp/2)+1):
		if inp%i == 0:
			return 0
	return 1
try:
	usr_input = int(input("Enter any number : "))
	if is_a_prime(usr_input):
		print("Given number is a prime number")
	else:
		print("Given number is not a prime number")
except ValueError:
	print("Please enter a number : ")