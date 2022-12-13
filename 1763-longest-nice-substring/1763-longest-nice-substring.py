class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        s = list(s)
        longest = ""        
        for i in range(len(s)):
            diction = {}
            for j in range(i, len(s)):
                key = s[j].lower()
                if key not in diction:
                    diction[key] = [s[j].isupper(), s[j].islower()]
                else:
                    diction[key] = \
                        [diction[key][0] or s[j].isupper(), diction[key][1] or s[j].islower()]
                
                valid = True
                for val in diction.values():
                    if val != [True, True]:
                        valid = False
                        break
                
                if valid and (j - i) >= len(longest):
                    longest = ''.join(s[i:j + 1])
            
        return longest