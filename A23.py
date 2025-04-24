# 23. Check if a number is an Armstrong number

no=input('enter a no ')
l=  int(no)==sum(map(lambda x:int(x)**len(no),no))
print("armstron ") if l else print("not armstrong")
# ?153  is armstronger

# z=[1,2,3,4,5]
# print(sum(z))