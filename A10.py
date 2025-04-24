# 10. Sort a list without using the built-in sort() method.
l=[1,3,5,2,3,6,7]
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    
print(l)