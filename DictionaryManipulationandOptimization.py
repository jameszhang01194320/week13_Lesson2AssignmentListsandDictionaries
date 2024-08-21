# Problem Statement: Explore advanced manipulation techniques and optimization strategies for Python dictionaries. Implement various dictionary operations and optimize them for improved performance.
# dict_1 = {
# 'pie': 'apple',
# 'ice_cream': 'moose tracks',
# 'cobbler': 'peach',
# 'cake': None
# }

# dict_2 = {
# 'dinner': 'turkey',
# 'ice_cream': 'vanilla',
# 'appetizer': 'soup',
# 'cobbler': 'peach'
# }
# Task 1
# •	Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time complexity of this operation.
# merged = {
# 'pie': 'apple',
# 'ice_cream': 'vanilla',
# 'cobbler': 'peach',
# 'cake': None,
# 'dinner': 'turkey,
# 'appetizer': 'soup'
# }
def merge_dictionaries(dict_1, dict_2):
    merged_dict = dict_1.copy()  # Start with a copy of dict_1
    merged_dict.update(dict_2)   # Update with dict_2, preserving its values for common keys
    return merged_dict

# Time Complexity:
# Copying dict_1 takes O(n) time, where n is the number of items in dict_1.
# Updating with dict_2 takes O(m) time, where m is the number of items in dict_2.
# Therefore, the overall time complexity is O(n + m).



# Task 2
# •	Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time complexity of this operation.
# intersection = {
# 'cobbler': 'peach'
# }

def intersect_dictionaries(dict_1, dict_2):
    intersection = {k: dict_1[k] for k in dict_1 if k in dict_2 and dict_1[k] == dict_2[k]}
    return intersection

# Time Complexity:

# Iterating over dict_1 takes O(n) time.
# Checking each key in dict_2 takes O(1) time (on average) due to the hashing mechanism in dictionaries.
# Therefore, the overall time complexity is O(n).