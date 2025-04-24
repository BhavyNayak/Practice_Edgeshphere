# 77. Write a function to check if a list is sorted.

l=[1,4,3,4,5,6]

def check_sorted(l):
    return all(l[i]<=l[i+1] for i in range(len(l)-1))
print(check_sorted(l))