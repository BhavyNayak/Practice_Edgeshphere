# 45. Reverse a list using a loop.
l=[x for x in range(11,20,2)]
l2=[l[i] for i in range(len(l)-1,-1,-1)]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
print(l2)