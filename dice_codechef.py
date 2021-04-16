no_of_testcases = int(input("Enter number of testcases : "))
no_of_dices_list = list()
non_visible_sides = list()
visible_dots = list()
sum_of_dots = list()
poss_val = (6,5,4,3,2,1)
sum1 = 0

no_of_complete_levels = 0

def sum(list1):
	sum1 = 0
	for i in list1:
		sum1 += i
	return sum1

def max(list1):
	max1 = 0
	for i in list1:
		if i > max1:
			max1 = i
	return max1

for i in range(no_of_testcases):
	no_of_dices_list.append(int(input("Enter number of dices : ")))

for testcase in range(no_of_testcases):
	visible_dots = []
	non_visible_sides = []
	dices = no_of_dices_list.pop()
	no_of_complete_levels = int(dices/4)
	dices_incomplete = dices%4

	if no_of_complete_levels:
		for level in range(no_of_complete_levels):
			for i in range(4):
				non_visible_sides.append(4)
		for i in range(4):
			non_visible_sides[i] -= 1
		if dices_incomplete:
			for i in range(dices_incomplete):
				non_visible_sides[i] += 1

	if dices_incomplete:
		if dices_incomplete > 1:
			for i in range(2):
				non_visible_sides.append(2)
			if dices_incomplete-2:
				non_visible_sides.append(3)
		else:
			non_visible_sides.append(1)

	for i in non_visible_sides:
		for j in range(6-i):
			visible_dots.append(poss_val[j])

	sum_of_dots.append(sum(visible_dots))


print(max(sum_of_dots))