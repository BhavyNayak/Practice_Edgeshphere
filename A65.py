# Find the length of the longest word in a sentence.
sen=input("enter a sent : ")

words=sen.split(" ")
# print(sorted(words,key=lambda x:len(x))[-1])
long_word=max(words,key=len)
print(long_word)
print(len(long_word))