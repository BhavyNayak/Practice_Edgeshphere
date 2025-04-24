# 20.List Rotation
# a. Given: A list of integers and a number k.
# Return: The list rotated to the right by k steps.
# Example:
# Input: [1, 2, 3, 4, 5], k = 2 → Output: [4, 5, 1, 2, 3]
def lst_rotation(l,k):
    
    t=l[-(k):]+l[:-(k)]
    return t
print(lst_rotation([1, 2, 3, 4, 5], k = 2))