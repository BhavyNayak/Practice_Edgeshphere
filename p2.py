# 2. Valid Palindrome 
# a. Given: A string. 
# Return: True if it is a palindrome, ignoring non-alphanumeric and case; else 
# False. 
# Example: 
# Input: "A man, a plan, a canal: Panama" → Output: True 

s='A man, a plan, a canal: Panama'
cod_S=''.join(list(filter(lambda c: c.isalnum(),s))).lower()
print(cod_S==cod_S[::-1])