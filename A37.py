# 37. Use a generator to yield even numbers.
# gen=(i for i in range(10))
# for i in range(10):
#     if i%2==0:
        
#         print ( next(gen))
#     else :
#        next(gen)
    

def gen(n):
    for i in range(n):
        yield(i)
g=gen(4)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))