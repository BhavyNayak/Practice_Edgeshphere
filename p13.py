# 13.Group By Type
# a. Given: A list of mixed types.
# Return: A dictionary grouping values by their type.
# Example:
# Input: [1, "a", 2.5, "b"] → Output: {int: [1], str: ["a",
# "b"], float: [2.5]}

Input= [1, "a", 2.5, "b"]
inp={}
for i in Input:
    key = type(i).__name__
    inp[key]=inp.get(key,[])
    inp[key].append(i)
    

print(inp)
