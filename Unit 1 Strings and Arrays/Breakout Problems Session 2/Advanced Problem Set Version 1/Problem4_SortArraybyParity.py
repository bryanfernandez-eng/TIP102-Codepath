
def sort_by_parity(nums):
    return [x for x in nums if x%2==0] + [x for x in nums if x%2==1] 

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))


# Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# def sort_by_parity(nums):
#     pass
# Example Usage

# nums = [3, 1, 2, 4]
# sort_by_parity(nums)

# nums = [0]
# sort_by_parity(nums)
# Example Output:

# [2, 4, 3, 1]
# [0]