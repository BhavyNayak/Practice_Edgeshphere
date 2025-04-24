# 55. Create a matrix and print its transpose.
# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose using list comprehension + zip
transpose = [list(row) for row in zip(*matrix)]

# Printing the transpose
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
