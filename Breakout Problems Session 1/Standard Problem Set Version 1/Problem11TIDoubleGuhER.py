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