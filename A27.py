# 27. Write a program to print a pattern (e.g., pyramid, triangle).
def pyramid(n):
     for i in range(n):
        for j in range(n,i,-1):
            print(" " , end='')
        for j in range(i):
            print("* ",end="")
        print()
pyramid(6)