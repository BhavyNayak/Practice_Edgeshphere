# 58. Sort a dictionary by its values

d={0: 0, 8: 64, 4: 16, 1: 1, 2: 4, 3: 9, 5: 25, 6: 36, 9: 81, 7: 49}
x= sorted(d.items(),key=lambda x: x[1])
print(dict(x))