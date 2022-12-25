class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        diction = {}
        
        left, right = 0, 0
        maxWindowSize = 0
        
        while right < len(s):
            diction[s[right]] = diction.get(s[right], 0) + 1
            
            maxFrequency = max(diction.values())
            windowSize = right - left + 1
            
            while windowSize - maxFrequency > k:
                diction[s[left]] -= 1
                left += 1
                windowSize = right - left + 1
            
            if windowSize - maxFrequency <= k:
                maxWindowSize = max(maxWindowSize, windowSize)
                right += 1
            
            
            
        return maxWindowSize