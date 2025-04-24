# 89. Compare performance of list vs set for membership testing.
import time
l=[i for i in range(10_000_000)]
s={i for i in range(10_000_000)}
# print(l)
# print(s)
start=time.time()
99999 in l

print(f"for list  {time.time()-start}")
start=time.time()

99999 in s
print(f"for set  {time.time()-start}")