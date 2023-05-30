class MyHashSet:

    def __init__(self):
        self.array = [ None for _ in range(10**6 + 1)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.array[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.array[key] = None

    def contains(self, key: int) -> bool:
        return self.array[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
