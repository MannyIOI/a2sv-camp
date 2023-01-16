class Solution:    
    def climbStairs(self, n: int) -> int:
        self.seen = {}
        return self.helper(n)
        
    def helper(self, n):
        if n in self.seen:
            return self.seen[n]

        if n <= 1:
            return 1
        
        self.seen[n] = self.helper(n - 1) + self.helper(n - 2)
        
        return self.seen[n]