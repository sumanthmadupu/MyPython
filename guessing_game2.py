#User will think of a number between 0 and 100
#the computer needs to guess that number,for every
#wrong guess made by the computer you have to tell it whether the number is 
#too low or too high or exact

max_num = 100
min_num = 0
attempt = 1
num_temp = 0
while(1):
	if (max_num-min_num)%2==0:
		num_temp = int((max_num-min_num)/2)
		print(num_temp)
	else:
		num_temp = int((max_num-min_num)/2)+1
		print(num_temp)
	usr_inp = int(input("Enter 0:match,1:high,-1:low : "))
	if usr_inp > 0:
		attempt += 1
		max_num = num_temp
	elif usr_inp < 0:
		attempt += 1
		min_num = num_temp
	else:
		print("I guessed in "+str(attempt)+" number of attempts")
		break