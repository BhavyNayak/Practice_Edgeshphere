# 7. Anagram Check
# a. Given: Two strings.
# Return: True if they are anagrams, else False.
# Example:
# Input: "listen", "silent" → Output: True
inp1='listen'
inp2='silent'
print(sorted(inp1.casefold())==sorted(inp2.casefold()))