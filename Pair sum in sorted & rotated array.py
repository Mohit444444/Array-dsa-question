# Input: arr[] = [11, 15, 6, 8, 9, 10], target = 16
# Output: true
# Explanation: There is a pair (6, 10) with sum 16.


# Input: arr[] = [11, 11, 15, 26, 38, 9, 10], target = 35
# Output: true
# Explanation: There is a pair (26, 9) with sum 35.


# Input: arr[] = [9, 10, 10, 11, 15, 26, 38], target = 45
# Output: false
# Explanation: There is no pair with sum 45.


def pairInSortedRotated(arr, target):  
    s = set()
    for num in arr:
      
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False