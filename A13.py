# 13. Check if two strings are anagrams.
str1='bhavy'
str2='avybh'


def check_anagrams(str1,str2):
    if len(str1)==len(str2) :
        for i in str1:
            if i not in (str2):
              print("both are not anagrams ")
              break
        else:
            print("both are anagrams")
check_anagrams(str1,str2)