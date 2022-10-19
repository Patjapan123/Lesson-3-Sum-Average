def sum_average(list):
	sum=0
	total=0
	all=0
	for i in range(0,len(list)):
		total = 0
		number=list[i]
		for j in number:
			total=j+total
		total1=total/len(number)
		#total equals all the numbers in this big cell
		sum=total1+sum
	return sum
		


Japan=[[4,3,2],[4,4],[1,1]]

print("the sum average is", sum_average(Japan))
	
	