# 71. Count the number of occurrences of a character in a string.
s1='ksjdbcle idjuncewidlufhncelwiudhcnew'
frq={}
for i in s1:
    frq[i]=frq.get(i,0)+1
print(frq)


frq2={k:s1.count(k) for k in set(s1)}
print(frq2)