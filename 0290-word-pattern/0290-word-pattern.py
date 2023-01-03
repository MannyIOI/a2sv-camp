class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_p_s = {}
        mapping_s_p = {}
        
        s = s.split(' ')
        
        if len(pattern) != len(s):
            return False
        
        for idx in range(len(s)):
            word = s[idx]
            letter = pattern[idx]
            
            if word not in mapping_s_p and letter not in mapping_p_s:
                mapping_p_s[letter] = word
                mapping_s_p[word] = letter
            
            elif word in mapping_s_p and mapping_s_p[word] != letter:
                return False
            elif letter in mapping_p_s and mapping_p_s[letter] != word:
                return False
        
        return True