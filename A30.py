# 30. Write a program to read and write to a text file
f=open('t1.txt','w+')
f.writelines("owucb oeidncl oidnc \njwhckwbckwjbcwejbc\niubcieurbceu")
f.seek(0)
print(f.read())
f.close()
