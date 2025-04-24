# 43. Implement a stack using a list.
class stack:
    def __init__(self,l):
        self.l=l
    def push(self,i):
        return self.l.insert(-1,i)
    def pop(self):
        return self.l.pop()
    def show_stack(self):
        print(self.l)
l=[1, 2, 3, 4, 5, 6, 66, 7, 77]
s1=stack(l)
s1.show_stack()
s1.push(1)
s1.show_stack()
s1.pop()
s1.show_stack()



