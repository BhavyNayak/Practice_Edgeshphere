# 59. Check if a given string is a valid palindrome (ignore cases and spaces).

def is_valid_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

# Example usage
print(is_valid_palindrome("A man a plan a canal Panama"))  # True
print(is_valid_palindrome("Hello"))                        # False
