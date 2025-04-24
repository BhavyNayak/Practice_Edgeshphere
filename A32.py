# 32. Write a program to append text to an existing file.
f=open("t1.txt",'a+')
# f.seek(-1)
f.write("kejrflcejl\niwecieubcu\niuecbeiucbe")
f.seek(0)
print(f.read())
f.close()