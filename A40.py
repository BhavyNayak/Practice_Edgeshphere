# 40. Use the map() function to convert a list of strings to integers.

l=['1','2','3','4','5','6','66','7','77']
s=map(lambda x: int(x),l)
print(l)
print(list(s))
# print(type(list(s)[0]))