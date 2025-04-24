# 8. Filter Non-None
# a. Given: A list with some None values.
# Return: A list with all None values removed.
# Example:
# Input: [1, None, 2, None, 3] → Output: [1, 2, 3]
Inpu= [1, None, 2, None, 3]
print(list(filter(lambda x:x!=None,Inpu)))