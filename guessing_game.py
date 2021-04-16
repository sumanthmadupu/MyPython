#guessing game
import random
comp_num = random.randint(1,9)

usr_inp = input("Guess a number between [1,9] : ")
attempt = 1
while(1):
	try:
		if comp_num > int(usr_inp):
			print("Go higher")
		elif comp_num < int(usr_inp):
			print("Go lower")
		else:
			print("Awesome.You got it in "+str(attempt)+" times")
			break
		attempt += 1
		usr_inp = input("Guess again...: ")
	except ValueError:
		if usr_inp.upper() == "EXIT":
			break
		else:
			print("type 'exit' to quit .")
			usr_inp = input()