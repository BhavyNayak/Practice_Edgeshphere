# 12. Find the frequency of elements in a list.
l=[1,2,3,4,5,6,7,3,5,6,3,4,6,2,4,6,7,4,6]

freq=dict()
for i in l:
    freq[i]=freq.setdefault(i,0)+1
print(freq)