class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        h = 0
        while left <= right:
            mid = (left + right) // 2
            
            toTheRight = len(citations) - mid
            
            if citations[mid] == toTheRight:
                return toTheRight
            
            if toTheRight > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
            
        return len(citations) - left