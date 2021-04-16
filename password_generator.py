#User will provide number of characters that the password should contain
#and also whether it should be a strong,medium or weak password

import random
import string

#def password_gen(size = 9,chars = string.ascii_letters+string.digits+string.punctuation):
#	return ''.join(random.choice(chars) for i in range(size))

def password_gen(size=9,chars = string.ascii_letters+string.digits+string.punctuation):
	return ''.join(random.sample(chars,size))

print(password_gen(int(input("Enter the number of characters your password should have : "))))