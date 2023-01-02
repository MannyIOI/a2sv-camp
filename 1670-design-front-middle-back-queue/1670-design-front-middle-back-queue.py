class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []
        

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = (len(self.arr) // 2)
        self.arr.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        if self.arr:
            return self.arr.pop(0)
        return -1

    def popMiddle(self) -> int:
        mid = (len(self.arr) // 2) - 1 if len(self.arr) % 2 == 0 else len(self.arr) // 2
        if self.arr:
            return self.arr.pop(mid)
        return -1

    def popBack(self) -> int:
        if self.arr:
            return self.arr.pop(-1)
        
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()