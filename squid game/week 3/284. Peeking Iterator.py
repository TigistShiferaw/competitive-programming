class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())
        # self.iterator.sort()
        self.index = 0

    def peek(self):
        return self.iterator[self.index]

    def next(self):
        ans = self.iterator[self.index]
        self.index += 1
        return ans

    def hasNext(self):
        if self.index  < len(self.iterator):
            return True
        return False