def count_less_than(race_times, threshold):
	count = 0 
	for num in race_times:
		if num < threshold: 
			count += 1 
	return count 
	
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))