from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for key in counter:
            if counter[key] > len(nums) // 2:
                return key
        
        