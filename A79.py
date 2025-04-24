# 79. Remove empty strings from a list.
s="           d v   r    r wrfr rerfe r ".split(' ')
s1=list(filter(lambda x:len(x)!=0 ,s))
# for i in s:
#     if len(i)==0:
#         s.remove()
print(s1)