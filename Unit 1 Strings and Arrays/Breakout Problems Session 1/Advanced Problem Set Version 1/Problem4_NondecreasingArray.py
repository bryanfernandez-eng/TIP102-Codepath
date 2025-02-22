def non_decreasing(nums):
    count = 0 
    for i in range(1, len(nums)): 
        if nums[i] < nums[i-1]: 
            count += 1 
            if count > 1: 
                return False 
            if i-2>=0 and nums[i] < nums[i-2]: 
                nums[i] = nums[i-1]
    return True 

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))


# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# def non_decreasing(nums):
# 	pass
# Example Usage:

# nums = [4, 2, 3]
# non_decreasing(nums)

# nums = [4, 2, 1]
# non_decreasing(nums)
# Example Output:

# True
# False