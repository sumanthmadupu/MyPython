#Takes a list as an input and will print another list with the elements less than 10

num = int(input("Enter the number of elements in the list : "))
inp_ls = list()
out_ls = list()
for i in range(num):
	inp_ls.append(int(input()))
	if inp_ls[i]<10:
		out_ls.append(inp_ls[i])

print("List with elements less than 10 : ",end="")
print(out_ls)