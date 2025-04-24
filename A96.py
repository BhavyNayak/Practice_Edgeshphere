# 96. Parse a JSON string and print values.
import json
json_str = '''
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}
'''
data = json.loads(json_str)
print(data)
print("Name:", data["name"])
print("Age:", data["age"])
print("Email:", data["email"])
print("Skills:", ", ".join(data["skills"]))
