def split_haycorns(quantity):
	arr = []
	for i in range(1, quantity+1): 
		if quantity % i == 0: 
			arr.append(i)
	return arr 

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))
