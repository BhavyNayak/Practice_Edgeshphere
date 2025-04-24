# 76. Use dictionary comprehension to invert keys and values.
d={'a':1,'b':2,'c':3}

d = list(zip(d.values(),d.keys()))
print(d)