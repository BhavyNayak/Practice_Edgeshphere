# write a python program to swap no./
def swap(a,b):
    t=a+b
    a=t-b
    b=t-a
    return a,b
# or 
def swap1(a,b):
    return b,a


print('swaped no of 10,11 by swap',swap1(10,11))
print('swaped no of 10,11 by swap1',swap(10,11))
