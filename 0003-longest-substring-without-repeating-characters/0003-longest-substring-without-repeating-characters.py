class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        diction = {}
        longest = 0
        curr = longest
        
        while right < len(s):
            
            diction[s[right]] = diction.get(s[right], 0) + 1
            
            while diction.get(s[right], 0) > 1 and left <= right:
                diction[s[left]] = diction.get(s[left], 0) - 1
                left += 1
                curr -= 1
            
            right += 1
            longest = max(right - left, longest)
        
        return longest
                