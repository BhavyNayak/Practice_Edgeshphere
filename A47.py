# 47. Find the most frequent element in a list.
# from collections import Counter 

# def most_freq_ele(l):
#     if not  l:
#         return None

#     count=Counter(l)
#     # print(count)
#     x=count.most_common(1)
#     # print(x)
#     return x

lst = [1, 2, 3,3,3,3,33, 1, 2, 1, 4, 5]
# print(most_freq_ele(lst))




def most_freq_elm(l):
    if not l :
        return None 
    return max(set(l),key= lambda x: l.count(x))
print(most_freq_elm(lst))