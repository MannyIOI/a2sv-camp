class MyHashSet:

    def __init__(self):
        self.keys = [False] * ((10 ** 6) + 2)

    def add(self, key: int) -> None:
        self.keys[key] = True

    def remove(self, key: int) -> None:
        self.keys[key] = False

    def contains(self, key: int) -> bool:
        return self.keys[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)