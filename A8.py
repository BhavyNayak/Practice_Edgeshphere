# Count the number of vowels in a string.

s=input("enter a string")
v=['a','e','i','o','u']
count=0
for i in s:
    if  i.lower() in v:
        count+=1    
print(count)
# print(s.count())