# 31. Count the number of lines in a text file

f=open('t1.txt','r')
print('lines count ',len(f.readlines()))
f.close()