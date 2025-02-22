def find_missing_clues(clues, lower, upper):
    res = []
    clues.append(upper+1)
    prev = lower-1 
    for n in sorted(clues): 
        if n > prev+1:
            res.append([prev+1, n-1])
        prev = n 
    return res      
      

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))



# Problem 5: Missing Clues
# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

# def find_missing_clues(clues, lower, upper):
#    pass
# Example Usage:

# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# find_missing_clues(clues, lower, upper)

# clues = [-1]
# lower = -1
# upper = -1
# find_missing_clues(clues, lower, upper)
# Example Output:

# [[2, 2], [4, 49], [51, 74], [76, 99]]
# []