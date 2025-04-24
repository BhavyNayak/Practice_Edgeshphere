# 99. Create a CLI-based todo list app.
l=[]
while True:
    x=int(input("enter a no 1> for add 2> for remove"))
    if x==1:
        l.append(input("enter a task"))
        for i in l:
            print(f"{l.index(i)}  : {i}")
            
        
    elif x==2:
        l.pop(int(input('enter a task index ')))
        for i in l:
            print(f"{l.index(i)}  : {i}")

            
    else :
        break
