# 17.Key Existence Checker
# a. Given: A dictionary and a key.
# Return: True if key exists, else False (without using in keyword).
# Example:
# Input: {"a":1}, "b" → Output: False
Input={"a":1}
k=list(Input.keys())
print(k.index('b'))