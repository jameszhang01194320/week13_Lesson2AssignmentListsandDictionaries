# Task 1: Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Time Complexity: The time complexity of this operation is O(n) because the function iterates over a range of n numbers and computes the square of each.
# Space Complexity: The space complexity is also O(n) since we are storing n squared values in the list.


# Task 2: Implement a function to merge two pre-sorted lists into a single sorted list
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements 
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))  # Should output: [1, 2, 4, 5, 6,30]

# Time Complexity: The time complexity is O(n + m), where n and m are the lengths of list1 and list2 respectively. The function iterates through both lists only once.