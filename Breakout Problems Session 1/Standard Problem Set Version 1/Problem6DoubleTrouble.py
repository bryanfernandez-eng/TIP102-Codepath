def doubled(hunny_jars):
	arr = []
	for i in range(len(hunny_jars)):
		arr.append(hunny_jars[i]*2)
	return arr

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))