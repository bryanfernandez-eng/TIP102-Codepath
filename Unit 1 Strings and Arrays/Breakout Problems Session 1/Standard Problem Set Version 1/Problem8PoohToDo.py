def print_todo_list(task):
    print("Pooh's To Dos:")
    for i, val in enumerate(task): 
        print(f"{i}. {val}")
	
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)


# Problem 8: Pooh's To Do's
# Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2
# ...

# def print_todo_list(task):
# 	pass
# Example Usage

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)
# Example Output:

# Pooh's To Dos:
# 1. Count all the bees in the hive
# 2. Chase all the clouds from the sky
# 3. Think
# 4. Stoutness Exercises

# Pooh's To Dos: