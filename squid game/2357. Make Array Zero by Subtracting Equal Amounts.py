class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            if n > 0:
                heappush(heap,n)
        count = 0
        while heap:
            x = heappop(heap)
            # print(x)
            temp = []
            for i in range(len(heap)):
                y = heappop(heap)
                if y - x > 0:
                    heappush(temp, y - x)
            count += 1
            heap = temp
        return count