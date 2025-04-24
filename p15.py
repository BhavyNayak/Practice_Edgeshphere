# 15.Most Frequent Value
# a. Given: A list of values.
# Return: The value that appears most frequently.
# Example:
# Input: [1,2,2,3] → Output: 2

from collections import Counter

Input = [1, 2, 2, 3]
counts = Counter(Input)
most_frequent = counts.most_common(1)[0][0]
print(most_frequent)
