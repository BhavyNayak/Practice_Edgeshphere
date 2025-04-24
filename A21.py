# 21. Write a program to check if a year is a leap year
y=int(input("enter a year "))
print("it is leap year") if y%4==0 or (y%400==0 and y%100) else print("it is not  leap year")
    