# 22. Find the sum of digits of a number.

no=input("enter a no ")
sm=0 
for i in no:
    sm+=int(i)
print(sm)


s=sum(map(lambda x:int(x),no))
print(s)
