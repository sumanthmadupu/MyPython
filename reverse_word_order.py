#Entere a sequence of words and I will print them in backwards

inp_str = input("Enter any string : ")

words_list = inp_str.split()

for i in range(len(words_list)):
	print(words_list[-i-1],"",end = "")