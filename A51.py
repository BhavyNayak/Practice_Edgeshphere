# 51. Use regex to validate an email address.
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# Test examples
emails = ["user@example.com", "hello.world@domain.co", "invalid@.com", "noatsign.com"]

for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
