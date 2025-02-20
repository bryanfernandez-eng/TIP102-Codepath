def sum_honey(hunny_jars):
	sum = 0 
	for num in hunny_jars:
		sum += num 
	return sum  


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))