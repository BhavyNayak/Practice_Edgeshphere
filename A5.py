# 5. Find the factorial of a number using recursion.
def fact(n):
    if n<=1:
        return 1
    else :
        return n*fact(n-1)
print(fact(5))