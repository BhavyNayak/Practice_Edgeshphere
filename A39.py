# 39. Write a program to remove punctuation from a string.
import string
def remove_punctulation(s):
    translator=str.maketrans('','',string.punctuation)
    return s.translate(translator)
s=input('enter a string : ')
print(f'before string is :{s} \n after string : {remove_punctulation(s)}')


# translator=str.maketrans('','',string.punctuation)
# s1=s.translate(translator)
# print(s1)