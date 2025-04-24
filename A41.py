# 41. Filter even numbers from a list using filter().
l=[1, 2, 3, 4, 5, 6, 66, 7, 77]
# s=filter(lambda x: x if x%2==0 else None ,l)
s=filter(lambda x: x%2==0 ,l)
print(list(s))