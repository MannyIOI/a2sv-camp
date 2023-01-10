"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = set()
        for i in range(1, z + 1):
            left, right = 1, z
            while left <= right:
                mid = (left + right) // 2
                if z > customfunction.f(i, mid):
                    left = mid + 1
                elif z < customfunction.f(i, mid):
                    right = mid - 1
                else:
                    ans.add((i, mid))
                    break
        
        return ans
        