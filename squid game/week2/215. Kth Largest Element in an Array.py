class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        small = min(nums)
        large = max(nums)
        arr = [False] * (large - small + 1)

        for i in range(len(nums)):
            arr[nums[i] - small] = True
            freq [nums[i]] += 1
        cnt = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == True:
                cnt += freq[i + small]
                if cnt >= k:
                    return i + small 
        if cnt >= k:
            return len(arr) - 1 + small 