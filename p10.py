# 10.Dict Merge
# a. Given: Two dictionaries.
# Return: A merged dictionary. In case of conflicts, values from the second
# dictionary should overwrite.
# Example:
# Input: {"a": 1}, {"a": 2, "b": 3} → Output: {"a": 2, "b": 3}

def mrg_dict(d1,d2):
    s=d1|d2
    return s

d1,d2={"a": 6}, {"a": 2, "b": 3}
print(mrg_dict(d1,d2))