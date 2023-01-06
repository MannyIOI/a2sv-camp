class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split(' ')
        
        for i in range(len(last) - 1, -1, -1):
            if len(last[i]) != 0:
                return len(last[i])
