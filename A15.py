# 15. Convert a list to a dictionary.

l=[1,2,4,6,7,5,4,6,3]
dic={i:y for i,y in enumerate(l)}
print(dic)

l=['a','b','c','d','e','e']
d=dict.fromkeys(l,0)
print(d)