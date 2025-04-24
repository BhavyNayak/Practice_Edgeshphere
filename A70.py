# Use recursion to calculate nth Fibonacci number.

# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else :
#         return n*fac(n-1)
    
# print(fac(3))

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)
    
n=int(input("enter nth term : "))
print(fibo(n))
print(list(fibo(i) for i in range(n+1)))