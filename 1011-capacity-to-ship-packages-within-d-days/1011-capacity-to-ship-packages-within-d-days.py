class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            
            calcDays = self.calculateDays(weights, mid)
            if calcDays <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
    def calculateDays(self, weights, capacity):
        current = 0
        days = 1
        for weight in weights:
            current += weight
            if current > capacity:
                days += 1
                current = weight
        
        return days