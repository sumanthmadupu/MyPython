#Takes a number as an input from the user and will print its divisors

num = int(input("enter any number : "))
div_list = list()
div_list.extend([1,num])
for i in range(2,int(num/2)+1):
	if num%i==0:
		div_list.append(i)
div_list.sort()
print("The divisors of the number "+str(num)+" are : ",end="")
print(*div_list)