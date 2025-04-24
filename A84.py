# 84. Use a lambda with reduce() to compute the product of a list.
from functools import reduce
print(reduce(lambda x,y:x*y , [i for i in range(1,10)]))