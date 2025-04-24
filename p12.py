# 12.Reverse Mapping
# a. Given: A dictionary.
# Return: A new dictionary with keys and values swapped.
# Example:
# Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}
Input= {"a": 1, "b": 2}
d=dict(zip(Input.values(),Input.keys()))
print(d)