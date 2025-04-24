# 95. Find the longest common prefix in a list of strings.
def find_longest_common_prefix(words):
	longest_common_prefix = words[0]
	for word in words[1:]:
		for i in range(len(longest_common_prefix)):
			if i >= len(word) or longest_common_prefix[i] != word[i]:
				longest_common_prefix = longest_common_prefix[:i]
				break

	return longest_common_prefix
words = ["geeksforgeeks", "geeks", "geek", "geezer"]
longest_common_prefix = find_longest_common_prefix(words)
print("The longest common prefix is:", longest_common_prefix)
