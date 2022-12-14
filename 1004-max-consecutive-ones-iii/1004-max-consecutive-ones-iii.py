class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        head, tail, ans, i = 0, 0, 0, 0
        while i < len(nums):
            if nums[i] == 1 or k > 0:
                tail += 1
                if nums[i] == 0:
                    k -= 1
                i += 1
            elif k == 0 and nums[i] == 0:
                if nums[head] == 0:
                    k += 1
                head += 1
            
            ans = max(ans, tail - head)
        
        return ans