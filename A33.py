# 33. Use try-except to handle divide-by-zero exception
a=int(input("enter a no1 : "))
b=int(input("enter a no2 : "))
try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)