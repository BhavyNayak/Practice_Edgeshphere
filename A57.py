# 57. Use datetime to calculate a person's age.
# from datetime import datetime

from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")  # e.g., '2000-04-22'
    today = datetime.today()
    age = today.year - birthdate.year

    return age
# Example usage
print("Age:", calculate_age("2000-04-22"))
