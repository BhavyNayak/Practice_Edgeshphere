# 34. Create a class to represent a Bank Account.

class Bank :
    def __init__(self,acno,name):
        self.acno=acno
        self.balance=0
        self.name=name
    def show_account(self):
        print(self.name)
        print(self.acno)
        print(self.balance)
Bank(1234,"bhavy").show_account()