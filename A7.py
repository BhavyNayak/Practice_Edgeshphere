# 7. Check if a string is a palindrome.
def check_palindrom(s):
    return s==s[::-1]
if check_palindrom(input("enter a string : ")):
    print("it is pal. ")
else:
    print("not a pla ")