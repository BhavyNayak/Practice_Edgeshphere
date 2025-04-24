# 28. Create a simple calculator using functions.
class Calculator:
    def sum(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def div(a,b):
        return a/b
    def mul(a,b):
        return a*b
    
opr=Calculator()
opr.sum(1,2)
opr.div(2,3)
opr.sub(5,4)
opr.mul(2,3)