
def merge_intervals(intervals):
    merged = []
    for interval in intervals: 
        if not merged or merged[-1][-1] < interval[0]: 
            merged.append(interval)
        else: 
            merged[-1][-1] = max(merged[-1][-1], interval[1])
    return merged 

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))

# Problem 6: Merge Intervals
# Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# def merge_intervals(intervals):
# 	pass
# Example Usage

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# merge_intervals(intervals)

# intervals = [[1, 4], [4, 5]]
# merge_intervals(intervals)
# Example Output:

# [[1, 6], [8, 10], [15, 18]]
# [[1, 5]]