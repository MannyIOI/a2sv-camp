import math
class Solution:
    def minSideJumps(self, obstacles):
        ans = [1, 0, 1]
        for i in range(len(obstacles)):
            print(obstacles[i], ans)
            if obstacles[i] == 0:
                min_val = min(ans)
                ans[0] = min_val + 1 if min_val < ans[0] else ans[0]
                ans[1] = min_val + 1 if min_val < ans[1] else ans[1]
                ans[2] = min_val + 1 if min_val < ans[2] else ans[2]

        
            else:
                ans[obstacles[i] - 1] = math.inf
                min_dist = min(ans)
                ans[obstacles[i] % 3] = min_dist + 1 if ans[obstacles[i] % 3] == math.inf else ans[obstacles[i] % 3]
                ans[(obstacles[i] + 1) % 3] = min_dist + 1 if ans[(obstacles[i] + 1) % 3] == math.inf else ans[(obstacles[i] + 1) % 3]

        return min(ans)


    def minSideJumps_1(self, obstacles, i = 0, curr=2) -> int:
#       Move forward if i + 1 is different from curr or i + 1 == 0
#       if i + 1 == curr then create two branches of minSideJumps_1 starting from i by the two alternatives
        # print(i, curr)
        if len(obstacles) == i + 1:
            return 0

        elif obstacles[i + 1] == 0 or obstacles[i + 1] != curr:
            return self.minSideJumps_1(obstacles, i + 1, curr)
        
        if obstacles[i + 1] == (self.custom_mod(curr + 1)) + 1:
#             return op2
            op2 = self.minSideJumps_1(obstacles, i, (self.custom_mod(curr + 2)))
            return op2 + 1
        elif obstacles[i + 1] == (self.custom_mod(curr + 2)) + 1:
#             return op1
            op1 = self.minSideJumps_1(obstacles, i, (self.custom_mod(curr + 1)))
            return op1 + 1
        else:
            op1 = self.minSideJumps_1(obstacles, i, (self.custom_mod(curr + 2)))
            op2 = self.minSideJumps_1(obstacles, i, (self.custom_mod(curr + 2)))
            return min(op1, op2) + 1
    
    def custom_mod(self, num):
        return ((num - 1) % 3) + 1

print(Solution().minSideJumps([0,0,3,1,0,1,0,2,3,1,0]))