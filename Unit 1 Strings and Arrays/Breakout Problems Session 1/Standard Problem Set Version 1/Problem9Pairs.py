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


# Problem 9: Pairs
# Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

# def can_pair(item_quantities):
# 	pass
# Example Usage

# item_quantities = [2, 4, 6, 8]
# can_pair(item_quantities)

# item_quantities = [1, 2, 3, 4]
# can_pair(item_quantities)

# item_quantities = []
# can_pair(item_quantities)
# Example Output:

# True
# False
# True