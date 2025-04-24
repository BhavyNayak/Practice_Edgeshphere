# 6. Reverse a string without using slicing.
strq=input("enter a string ")
# print(strq[::-1])
# for i in range(len(strq)-1,-1,-1):
#     print(strq[i],end='')


t=list(strq)
t.reverse()
print(''.join(t))
