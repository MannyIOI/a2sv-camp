class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostK(nums, k) - self.atmostK(nums, k - 1)
    
    def atmostK(self, nums, k):
        diction = {}
        left = 0
        ans = 0
        
        
        for right in range(len(nums)):
            diction[nums[right]] = diction.get(nums[right], 0) + 1
            
            while len(diction) > k:
                diction[nums[left]] = diction.get(nums[left], 0) - 1
                if diction[nums[left]] == 0:
                    del diction[nums[left]]
                
                left += 1
            
            ans += right - left + 1
            
        
        return ans