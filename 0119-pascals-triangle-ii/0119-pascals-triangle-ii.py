class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [[1]]
        
        for i in range(1, rowIndex + 1):
            row.append([1])
#             do processing

            for j in range(1, i):
                val = row[i - 1][j - 1] + row[i - 1][j]
                row[-1].append(val)
            row[-1].append(1)
            
        
        return row[-1]