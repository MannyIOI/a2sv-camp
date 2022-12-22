class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        left, right = 0, 0
        diction = {}
        
        while right < len(fruits):
            if fruits[right] in diction or len(diction.keys()) < 2:
                diction[fruits[right]] = diction.get(fruits[right], 0) + 1
                right += 1
                res = max(right - left, res)
            else:
                while len(diction.keys()) == 2:
                    diction[fruits[left]] -= 1
                    
                    if diction[fruits[left]] == 0:
                        del diction[fruits[left]]

                    
                    left += 1
        
        return res