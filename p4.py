# 4. Find Unique Integers 
# a. Given: A list of integers where every element appears twice except one. 
# Return: That unique element. 
# Example: 
# Input: [2, 2, 1] → Output: 1 


l=[2,2,1,4,5,5,6]
print(list(filter(lambda x: l.count(x)==1, l)))
