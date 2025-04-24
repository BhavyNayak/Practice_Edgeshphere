# 97. Serialize a dictionary to JSON and write to a file.
import json
x={
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}
data=json.dumps(x)
with open('json1.txt','w') as f:
    f.write(data)
    f.close()