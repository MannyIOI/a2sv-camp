class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
#         3, 2, 4, 1
    
        nums = A
        ans = []
        while len(nums) > 0:
            idx = nums.index(max(nums))
            ans.append(idx + 1)
            ans.append(len(nums))
            
            nums = nums[idx + 1:][::-1] + nums[0: idx]
        
        return ans