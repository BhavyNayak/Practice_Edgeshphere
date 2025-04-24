# 42. Write a function that returns the factorial using memoization.
def factorial_memorize(n,memo={}):
    if n in memo:
        return memo[n]
    if n==0 or n==1:
        return 1
    memo[n]=n*factorial_memorize(n-1,memo)
    return memo[n]

print(factorial_memorize(5))