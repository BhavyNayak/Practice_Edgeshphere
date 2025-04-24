# 19. Convert a string to title case without using title().
s=input("enter a string ")
word=s.split(" ")
title=' '.join([i[0].upper()+i[1:] for i in word])
print(title)