class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]] * len(w)
        for i in range(1,len(w)):
            self.prefix[i] = w[i] + self.prefix[i - 1]

    def pickIndex(self) -> int:

        index = random.uniform(0,self.prefix[-1])
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = left + (right - left) // 2
            if self.prefix[mid]  < index:
                left = mid  + 1
            else:
                right = mid
        return left
