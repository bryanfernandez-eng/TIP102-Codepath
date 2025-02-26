# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# def three_sum(nums):
#     pass
# Example Usage

# nums = [-1, 0, 1, 2, -1, -4]
# three_sum(nums)

# nums = [0, 1, 1]
# three_sum(nums)

# nums = [0, 0, 0]
# three_sum(nums)
# Example Output:

# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]


def three_sum(nums):
    nums.sort()
    res=[]
    for i, a in enumerate(nums): 

        if a > 0: break 
        if i > 0 and nums[i-1] == a: 
            continue 
        l = i+1
        r = len(nums)-1
        while l < r: 
            cur_sum = a + nums[r] + nums[l]
            if cur_sum < 0:
                l += 1 
            elif cur_sum > 0: 
                r -= 1 
            else: 
                res.append([a, nums[l], nums[r]])
                l += 1 
                r -= 1 
                while l < r and nums[l] == nums[l-1]: 
                    l += 1
                
    print(res)
    return res
                
    

nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)