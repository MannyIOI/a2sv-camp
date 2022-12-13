from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dc = defaultdict(list)
        
        for i in range(len(nums)):
            dc[nums[i]].append(i)
        
        for num in dc:
            if len(dc[num]) > 1:
                for i in range(1, len(dc[num])):
                    if abs(dc[num][i - 1] - dc[num][i]) <= k:
                        return True
        
        return False