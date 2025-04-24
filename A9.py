# 9. Find the largest and smallest elements in a list.
l=[1,3,5,0,3]
# l.sort()
# min,max=l[0],l[-1]
# print(max , min )

min=max=l[0]
for i in l :
    if i <min:
        min=i
    if i>max:
        max=i
print(min,max)