def harvest(vegetable_patch): 
    count = 0 
    for row in range(len(vegetable_patch)):
        for col in range(len(vegetable_patch[0])): 
            if vegetable_patch[row][col] == 'c':
                count += 1 
    return count  


vegetable_patch = [
 	['x', 'c', 'x'],
 	['x', 'x', 'x'],
 	['x', 'c', 'c'],
 	['c', 'c', 'c']
 ] 
print(harvest(vegetable_patch))

# Problem 6: Vegetable Harvest
# Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

# Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

# def harvest(vegetable_patch):
# 	pass
# Example Usage:

# vegetable_patch = [
# 	['x', 'c', 'x'],
# 	['x', 'x', 'x'],
# 	['x', 'c', 'c'],
# 	['c', 'c', 'c']
# ]
# harvest(vegetable_patch)
# Example Output:

# 6