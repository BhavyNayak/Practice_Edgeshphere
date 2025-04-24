# for i in range(2,21):
#     with open(f'p{i}.py','w') as f:
#         f.write('')
#         f.close()

# 1. Character Frequency Counter 
# a. Given: A string. 
# Return: A dictionary with the frequency of each character. 
# Example: 
# Input: "hello" → Output: {'h':1, 'e':1, 'l':2, 'o':1} 

s=input("enter a string : ")
frq={}

for c in s:
    frq[c]=frq.setdefault(c,0)+1
print(frq)