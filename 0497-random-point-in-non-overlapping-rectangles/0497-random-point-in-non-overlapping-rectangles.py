import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]

    def pick(self) -> List[int]:
        rect = random.choices(self.rects, self.weights)[0]
        
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]
       


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()