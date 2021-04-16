#Rock , Paper , Scissors game
#User will select one , computer will select one and it will
#announce the winner

import os
import random

play = 'y'

def declare_result(usr_ch,comp_ch):
	if usr_ch == 0:
		if comp_ch == 0:
			print("User : Rock , Computer : Rock")
			return 0
		elif comp_ch == 1:
			print("User : Rock , Computer : Paper")
			return -1
		elif comp_ch == 2:
			print("User : Rock , Computer : Scissors")
			return 1
	elif usr_ch == 1:
		if comp_ch == 0:
			print("User : Paper , Computer : Rock")
			return 1
		elif comp_ch == 1:
			print("User : Paper , Computer : Paper")
			return 0
		elif comp_ch == 2:
			print("User : Paper , Computer : Scissors")
			return -1
	elif usr_ch == 2:
		if comp_ch == 0:
			print("User : Scissors , Computer : Rock")
			return -1
		elif comp_ch == 1:
			print("User : Scissors , Computer : Paper")
			return 1
		elif comp_ch == 2:
			print("User : Scissors , Computer : Scissors")
			return 0
	else:
		return 0

while(play == 'y'):
	os.system("clear")
	print("Rock		: 0")
	print("Paper	: 1")
	print("Scissors	: 2")
	try:
		user_choice = int(input("Please choose one of the options (Enter the corresponding number) : "))
		user_choice = user_choice%3
	except:
		print("Please enter a correspoonding number,nothing else")
	comp_choice = random.randint(0,2)
	if(declare_result(user_choice,comp_choice) == 0):
		print("DRAW")
	elif(declare_result(user_choice,comp_choice) > 0):
		print("YOU WON")
	else:
		print("COMPUTER WON")
	play = input("Do you want to play again? 'y' or 'n' : ")
	if play != 'y':
		break