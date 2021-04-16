#Here two lists with random numbers will be generated and 
#will print a list with numbers that are in both the lists and 
#unique in both the lists
#My code might be bad.I'm just a beginner so please ignore it.
import random

def make_unique(lst):
	for i in lst:
		if lst.count(i)>1:
			for j in range(lst.count(i)-1):
				lst.remove(i)
list1 = [random.randint(1,9) for i in range(random.randint(1,9))]
list2 = [random.randint(1,9) for i in range(random.randint(1,9))]

intersection_list = list()
unique_list = list()
list_temp = list()

intersection_list = [i for i in list1 if i in list2]

list_temp = [i for i in list1 if i not in list2]
unique_list = [i for i in list2 if i not in list1]
unique_list = [*unique_list,*list_temp]

make_unique(intersection_list)
make_unique(unique_list)

print("list1 : ",end="")
print(list1)
print("list2 : ",end="")
print(list2)
print("intersection_list : ",end="")
print(intersection_list)
print("unique_list : ",end="")
print(unique_list)