# 5. Tuple Swap
# a. Given: A tuple (a, b)
# Return: A new tuple with values swapped.
# Example:
# Input: (5, 10) → Output: (10, 5)

def swap_tuple(t):
    return t[::-1]
print(swap_tuple((1,2)))