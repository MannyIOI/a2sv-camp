class RecentCounter:

    def __init__(self):
        self.timestamps = []
        self.currIdx = 0

    def ping(self, t: int) -> int:
        self.timestamps.append(t)
        while self.timestamps[self.currIdx] < (t - 3000):
            self.currIdx += 1
        
        return len(self.timestamps) - self.currIdx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)