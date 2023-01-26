class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
#         ans = []
        
#         while columnNumber > 26:
#             rem = columnNumber % 26
#             columnNumber = columnNumber // 26
#             if rem == 0:
#                 ans.append('Z')
#             else:
#                 ans.append(chr(ord('A') + rem - 1))

#         columnNumber -= 1
#         ans.append(chr(ord('A') + columnNumber))
#         return ''.join(ans[::-1])
    
        num = columnNumber
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
        