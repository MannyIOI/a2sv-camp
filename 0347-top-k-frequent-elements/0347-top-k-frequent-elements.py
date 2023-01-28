class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = collections.Counter(nums)
        countHeap = []
        
        for key in countDict:
            heapq.heappush(countHeap, (countDict[key], key))
            
            if len(countHeap) > k:
                heapq.heappop(countHeap)

        
        return [val for count, val in countHeap]