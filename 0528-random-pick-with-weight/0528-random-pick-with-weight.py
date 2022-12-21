class Solution:

    def __init__(self, w: List[int]):
        self.pSum = list(accumulate(w))
        

    def pickIndex(self) -> int:
        target = random.random() * self.pSum[-1]
        
        low, high = 0, len(self.pSum)
        
        while low <= high:
            mid = low + (high - low) // 2
            if target > self.pSum[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
        
        

# [1, 4, 8, 100]

5
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()