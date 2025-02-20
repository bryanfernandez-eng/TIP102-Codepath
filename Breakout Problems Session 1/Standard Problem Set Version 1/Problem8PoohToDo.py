def print_todo_list(task):
    print("Pooh's To Dos:")
    for i, val in enumerate(task): 
        print(f"{i}. {val}")
	
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)