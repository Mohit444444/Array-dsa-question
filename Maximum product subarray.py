# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod1 = nums[0]
        prod2 = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
            prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
            prod1 = temp

            result = max(result, prod1)

        return result

        # Time Complexity: O(N)
        # Space Complexity: O(1)
