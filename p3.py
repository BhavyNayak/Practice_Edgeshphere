# 3. List to Dictionary 
# a. Given: Two lists, one of keys and one of values. 
# Return: A dictionary mapping keys to values. 
# Example: 
# Input: ["a", "b"], [1, 2] → Output: {"a":1, "b":2

l1=['a','b','c','d','e']
l2=[n for n in range(len(l1))]

print(dict(zip(l1,l2)))