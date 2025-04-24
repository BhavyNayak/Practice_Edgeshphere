# 92. Write a simple login system (username & password).
def login(username,pwd):
    cusername='bhavy'
    cpwd='1234'
    if cusername==username and cpwd==pwd:
        print("welcome to this page : ")

print("login page ")
login(input("enter a username :"),input("enter a password : "))