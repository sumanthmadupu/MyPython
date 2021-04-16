#Creating a random list and removing the duplicates
import random

ls = [random.randint(1,9) for i in range(1,18)]

def make_unique(list1):
	temp_list = list()
	for i in list1:
		if i not in temp_list:
			temp_list.append(i)
	return temp_list

print("Before : ",ls)
print("After : "make_unique(ls))