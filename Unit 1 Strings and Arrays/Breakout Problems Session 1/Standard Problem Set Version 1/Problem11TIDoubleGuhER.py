def tiggerfy(s):
    exclusive = {'t', 'i', 'g', 'e', 'r'}
    arr = []
    
    for char in s:
        if char.lower() not in exclusive:
            arr.append(char)
    return "".join(arr) 

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"

print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))


# Problem 11: T-I-Double Guh-ER
# Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

# def tiggerfy(s):
# 	pass
# Example Usage

# s = "suspicerous"
# tiggerfy(s)

# s = "Trigger"
# tiggerfy(s)

# s = "Hunny"
# tiggerfy(s)
# Example Output:

# "suspcous"
# ""
# "Hunny"