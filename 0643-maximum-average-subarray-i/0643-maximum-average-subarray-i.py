class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pSum = [0]
        for num in nums:
            pSum.append(pSum[-1] + num)
            
        maxAvg = pSum[k] / k
        for i in range(k, len(pSum)):
            avg = (pSum[i] - pSum[i - k])/k
            maxAvg = max(maxAvg, avg)
        
        return maxAvg