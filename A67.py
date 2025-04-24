# 67. Print a multiplication table using nested loops.
l=[[i*j for j in range(1,11)] for i in range(1,11)]
print(l)

# for i in range(1, 11):       # Rows: 1 to 10
#     for j in range(1, 11):   # Columns: 1 to 10
#         print(f"{i*j:4}", end="")  # Print with spacing
#     print()  # Newline after each row
