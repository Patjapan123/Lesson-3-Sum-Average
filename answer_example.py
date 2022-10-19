def sum_average(list): #a function that give the sum average of a list
	sum = 0 # sum starts at 0
	for sublist in list: # sublist( the list in list )
		sublist_sum = 0 #sublist sum is 0 it starts at 0 every time of the loop
		for x in sublist: # each term in sublist 
			sublist_sum += x # all the term in sublist add each other
		sum += sublist_sum / len(sublist) 
		# the average of the sublist equal to sum
		# then sum is then added to another average of sublist from another term in the list
	return sum # return the sum average of the list