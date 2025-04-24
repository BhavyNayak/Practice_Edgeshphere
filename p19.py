# 19.Replace Elements with Greatest on Right
# a. Given: A list of integers.
# Return: A list where each element is replaced with the greatest element
# among the elements to its right. The last element should be -1.
# Example:
# Input: [17, 18, 5, 4, 6, 1] → Output: [18, 6, 6, 6, 1, -1]
def greatest_right(l):
    for i in range(len(l)-1):
        l[i]=max(l[(i+1):])
    l[-1]=-1
    return l
print(greatest_right([17, 18, 5, 4, 6, 1]))