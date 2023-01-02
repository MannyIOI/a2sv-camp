class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        
        while num > 0:
            x, num = self.helper(num)
            ans += x
        
        return ans
    
    def helper(self, num):
        if num >= 1000:
            return 'M', num - 1000
        elif num >= 900:
            return 'CM', num - 900
        elif num >= 500:
            return 'D', num - 500
        elif num >= 400:
            return 'CD', num - 400
        elif num >= 100:
            return 'C', num - 100
        elif num >= 90:
            return 'XC', num - 90
        elif num >= 50:
            return 'L', num - 50
        elif num >= 40:
            return 'XL', num - 40
        elif num >= 10:
            return 'X', num - 10
        elif num >= 9:
            return 'IX', num - 9
        elif num >= 5:
            return 'V', num - 5
        elif num >= 4:
            return 'IV', num - 4
        elif num >= 1:
            return 'I', num -1
        elif num == 0:
            return '-'