# 16.Longest Word
# a. Given: A string containing multiple words.
# Return: The longest word.
# Example:
# Input: "This is OpenAI GPT" → Output: "OpenAI"
Input= "This is OpenAI GPT"
print(max(Input.split(' '),key=len))