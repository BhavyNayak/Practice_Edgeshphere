# 3. Write a program to check if a number is prime.
x=int(input("enter a no "))

def chekno(n):
        
    dv_by=[]
    for i in range(1,n+1):
        if n%i==0 :
            dv_by.append(i)
        else:
            pass

    print(dv_by)
    if len(dv_by)<=2:
        
        print("no is  prime")
        
    else :
        print("no is not prime ")
chekno(x)