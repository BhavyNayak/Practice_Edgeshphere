# 18.Safe List Index
# a. Given: A list and an index.
# Return: Element at the index or "Index Out of Range" safely.
# Example:
# Input: [1, 2, 3], 5 → Output: "Index Out of Range"
def Safe_List_Index(str):
    if len(str.split('[')[1].split(']')[1])!=0 :
        print('idex out of range ')
    else :
        print("it is perfect ")
Safe_List_Index('[1, 2, 3],5')