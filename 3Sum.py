# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

                
            lo, hi = i+1, n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
        
        return answer
        # Time: O(n^2)
        # Space: O(n) (Excluding the output)
                    

                