def can_pair(item_quantities):
	for i in item_quantities: 
		if i % 2 == 1: 
			return False 
	return True 


item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))
