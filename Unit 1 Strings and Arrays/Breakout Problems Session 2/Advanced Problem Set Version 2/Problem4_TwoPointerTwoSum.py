# Use the two pointer approach to implement a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

# def two_sum(nums, target):
#     pass
# Example Usage

# nums = [2, 7, 11, 15]
# target = 9
# two_sum(nums, target)

# nums = [2, 7, 11, 15]
# target = 18
# two_sum(nums, target)
# Example Output:

# [0, 1]
# [1, 2]

def two_sum(nums, target):
    l = 0 
    r = len(nums)-1
    while l < r: 
        cur_sum = nums[l] + nums[r]
        if cur_sum == target: 
            print([l,r])
            return [l, r]
        elif cur_sum < target: 
            l += 1 
        else: 
            r -= 1 

nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target)