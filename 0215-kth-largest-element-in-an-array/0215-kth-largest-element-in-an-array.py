class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapArray = []
        
        for num in nums:
            heapq.heappush(heapArray, num)
            if len(heapArray) > k:
                heapq.heappop(heapArray)
        
        return heapArray[0]