# 14.JSON Key Extractor
# a. Given: A nested dictionary.
# Return: All keys at all levels in a flat list.
# Example:
# Input: {"a": 1, "b": {"c": 2}} → Output: ["a", "b", "c"]

def json_extractor(d):
    key=[]
    for i,v in d.items():
       key.append(i)
       if isinstance(v,dict):
           key.extend(json_extractor(v))
    return key
print(json_extractor({"a": 1, "b": {"c": 2, "d": {"e": 3}}}))