class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        diction = {}
        ans = set()
        for num in nums:
            diction[num] = diction.get(num, 0) + 1
            if diction.get(num, 0) > (len(nums) // 3):
                ans.add(num)
        
        return ans
        