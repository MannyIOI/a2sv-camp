class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            rem = (columnNumber - 1) % 26
            ans.append(chr(ord('A') + rem))
            columnNumber = (columnNumber - 1) // 26

        ans.reverse()
        return ''.join(ans)
    
#         num = columnNumber
#         capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
#         result = []
#         while num > 0:
#             result.append(capitals[(num-1)%26])
#             num = (num-1) // 26
#         result.reverse()
#         return ''.join(result)
        