# 98. Validate a phone number using regular expressions.
import re
def is_valid_phone(number):
    pattern = r'^[6-9]\d{9}$' 
    return re.fullmatch(pattern, number) is not None
phone = input("Enter phone number: ")
print("Valid phone number")if is_valid_phone(phone) else print(" Invalid phone number")
    

    

        