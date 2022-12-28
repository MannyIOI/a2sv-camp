class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        
        s = list(s)
        
        for i in range(10, len(s) + 1):
            curr = ''.join(s[i - 10:i])
            
            if curr in seen:
                ans.add(curr)
            else:
                seen.add(curr)
        
        return ans