# Examples:
# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and smallest positive missing number is 1.

# Input: arr[] = [1, 3, 3] 
# Output: [3, 2]
# Explanation: Repeating number is 3 and smallest positive missing number is 2.

# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5]
# Explanation: Repeating number is 1 and the missing number is 5.

# def find_missing_and_repeating(arr):
#     n = len(arr)
#     # Initialize variables for missing and repeating
#     repeated = -1
#     missing = -1
    
#     # Mark elements visited
#     for i in range(n):
#         index = abs(arr[i]) - 1
#         # If the value at the index is negative, it means this number is repeated
#         if arr[index] < 0:
#             repeated = abs(arr[i])
#         else:
#             arr[index] = -arr[index]
    
#     # Check for the missing number
#     for i in range(n):
#         if arr[i] > 0:
#             missing = i + 1
    
#     return repeated, missing

# # Example usage
# arr = [4, 3, 6, 2, 1, 1]  # Example input
# repeated, missing = find_missing_and_repeating(arr)
# print(f"Repeated: {repeated}, Missing: {missing}")


class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        repeated = -1
        missing = -1
    
    
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                repeated = abs(arr[i])
            else:
                arr[index] = -arr[index]
    
   
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
    
        return repeated, missing
    
    