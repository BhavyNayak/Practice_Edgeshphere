# 38. Use a lambda function to sort a list of tuples.
l=[(1,2),(3,7),(2,4),(7,8),(3,5),(8,4)]
z=sorted(l,key=lambda x:x[0])
print(z)