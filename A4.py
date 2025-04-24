# # 4. Generate the Fibonacci sequence up to n terms.
# def fibo(n):
#     if n==0:
        
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    

# def fibo(n,a=0,b=1):
#     if n==0:
#         return 
#     else:
#         print(a,b,end=',')
#         return fibo(n-1,b,a+b) 
    
# # print(fibo(12))
# fibo(12)

def fibo(n):
    a=0
    b=1
   
    print(a,b,end=',')
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c,end=',')
fibo(12)