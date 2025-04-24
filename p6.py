# 6. Flatten Nested List (use recursion)
# a. Given: A nested list of integers.
# Return: A flat list.
# Example:
# Input: [[1,2], [3,4]] → Output: [1, 2, 3, 4]

nl=[[1,2], [3,4]]
def rec_Flatten(nl):
    l=[]
    for i in nl:
        if isinstance(i,list):
            l.extend( rec_Flatten(i))
        else:
            l.append(i)
    return l
print(rec_Flatten(nl))
