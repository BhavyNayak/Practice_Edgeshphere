# 14. Merge two dictionaries.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car1 = {
"brand": "TATA",
"model": "Safari",
"year": 1965
}

d1={1:'1',2:'2',3:'3.'}
d2={11:'11',22:'22',33:'33'}
# d1.update(d2)
merged=d1|d2
print(merged)
