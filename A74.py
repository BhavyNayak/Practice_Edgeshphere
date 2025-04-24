# 74. Write a program to convert binary to decimal.
def bin_to_decimal(binary_s):
    return int(binary_s,2)

print(f"decimal no : {bin_to_decimal(input("enter a no in binary : "))}")