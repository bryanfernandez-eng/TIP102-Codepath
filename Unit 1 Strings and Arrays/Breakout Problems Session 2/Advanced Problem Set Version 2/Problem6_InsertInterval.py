# Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.

# Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# You don't need to modify intervals in-place. You can make a new array and return it.

# def insert_interval(intervals, new_interval):
#     pass
# Example Usage

# intervals = [[1, 3], [6, 9]]
# new_interval = [2, 5]
# insert_interval(intervals, new_interval)

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# new_interval = [4, 8]
# insert_interval(intervals, new_interval)
# Example Output:

# [[1, 5], [6, 9]]
# [[1, 2], [3, 10], [12, 16]]


def insert_interval(intervals, new_interval):
    result = []
    i = 0 
    
    while i < len(intervals) and intervals[i][1] < new_interval[0]: 
        result.append(intervals[i])
        i += 1 
    
    while i < len(intervals) and intervals[i][0] <= new_interval[1]: 
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1 
    
    result.append(new_interval)
    
    while i < len(intervals): 
        result.append(intervals[i])
        i += 1 
    
    print(result) 
    return result 
    


intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)
