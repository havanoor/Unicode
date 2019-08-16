
input_string=input()

input_list=input_string.split(',')


for i in input_list:
	dec=int(i,2)
	if (dec%5==0):
		print(i,end=",")