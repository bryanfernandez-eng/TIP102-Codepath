def get_item(items, x):
    if x < len(items): 
        return f'"{items[x]}"'
    return None 

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))