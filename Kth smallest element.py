# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
# Output: 7


# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
# # Output: 10 

import heapq
class Solution:

    def kthSmallest(self, arr,k):
        max_heap = []
    
        for num in arr:
            heapq.heappush(max_heap, -num)

      
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return -max_heap[0]
        
        # time O(N * log K)
        # space O(K)
        