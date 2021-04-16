#Takes a string input from the user an will tell whether
#it is a palindrome string or not

def check_for_spaces(string):
	if ' ' in string:
		return 1
	else:
		return 0

def is_palindrome(string):
	non_palindrome = int()
	for i in range(int(len(string)/2)):
		if string[i] != string[-i-1]:
			non_palindrome = 1
	return not non_palindrome

usr_str = input("Enter a string without any spaces : ")

if(check_for_spaces(usr_str)):
	print("Please enter the string by removing the spaces")
elif(is_palindrome(usr_str)):
	print("Given string is a palindrome string")
else:
	print("Given string is not a palindrome")