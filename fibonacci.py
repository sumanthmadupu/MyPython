#Asks the user to enter how many numbers in the
#series that I have to produce

def generate_fibonacci(num):
	fibo_list = [0,1]
	for i in range(num-2):
		fibo_list.append(fibo_list[-1]+fibo_list[-2])
	return fibo_list
try:
	usr_inp = int(input("Enter how many fibonacci numbers should I produce : "))
	fibonacci_list = list()
	fibonacci_list = generate_fibonacci(usr_inp)
	print(fibonacci_list)
except ValueError:
	print("You didn't entered a number.")