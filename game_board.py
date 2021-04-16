#User will give the size of one side and this will print the ame board

size = int(input("Enter the size of the board(ex:if 6X6, enter 6) : "))

for i in range(size):
	print("-"*(size*3))
	print("|  "*(size+1))

print("-"*size*3)