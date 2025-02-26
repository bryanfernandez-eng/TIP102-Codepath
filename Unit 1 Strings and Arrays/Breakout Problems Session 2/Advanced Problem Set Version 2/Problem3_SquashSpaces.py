# Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.

# def squash_spaces(s):
#     pass
# Example Usage

# s = "   Up,     up,   and  away! "
# squash_spaces(s)

# s = "With great power comes great responsibility."
# squash_spaces(s)
# Example Output:

# "Up, up, and away!"
# "With great power comes great responsibility."

def squash_spaces(s):
    res = []
    space_seen = False 
    for char in s: 
        if char == " ":
            if not space_seen and res: 
                res.append(char)
                space_seen = True 
        else: 
            res.append(char)
            space_seen = False 
    if res and res[-1] == " ": 
        res.pop()
            
    print("".join(res))
    return "".join(res)


s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)