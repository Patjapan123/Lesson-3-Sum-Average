import code

if code.sum_average([[4,5,6],[1,2]]) == 6.5:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed! [[4,5,6],[1,2]] expected 6.5, got", code.sum_average([[4,5,6],[1,2]]))

if code.sum_average([[4,5,9],[1,2],[0,0]]) == 7.5:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed! [[4,5,9],[1,2],[0,0]] expected 7.5, got", code.sum_average([[4,5,9],[1,2],[0,0]]))
