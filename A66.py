# Count uppercase and lowercase letters in a string.
s1="hbvhbJHBLJHbljh ljhcd kjd"
up=0
lw=0
for chr in s1:
    if chr.isupper():
        up+=1
    elif chr.islower():
        lw+=1
print(f"upercase  chr {up}")
print(f"lowercase  chr {lw}")