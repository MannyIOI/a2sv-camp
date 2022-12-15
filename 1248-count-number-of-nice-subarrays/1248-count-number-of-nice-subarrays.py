class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref=list(accumulate([0 if num%2==0 else 1 for num in nums]))
        
        diction={0: 1}
        res=0
        
        
        for num in pref:
            if num - k in diction:
                res+=diction[num-k]
            diction[num] = diction.get(num, 0) + 1
        return res