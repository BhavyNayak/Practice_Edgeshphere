# 68. Implement a binary search algorithm.


# def binary_search_algo(l,x):
#     low=0
#     high=len(l)
#     while low<=high:
#         mid=(low+high)//2
#         if l[mid]==x:
#             return mid
#         elif l[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
        
# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7

# result = binary_search_algo(arr, target)

# if result != -1:
#     print(f"Found at index {result}")
# else:
#     print("Not found")




def binary_search(l,n,mid=None):
    if mid== None:
        mid=len(l)//2

    if l[mid]==n:
        return mid
    elif l[mid]<n:
        return binary_search(l,n,mid=mid+1)
    elif l[mid]>n:
        return binary_search(l,n,mid=mid-1)
    else :
        return -1
    
arr = [1, 3, 5, 7, 9, 11, 13]
target = 13

print(binary_search(arr, target))