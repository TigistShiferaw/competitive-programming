class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0]
        tot = 0
        for n in nums:
            if tot < 0:
                tot = 0
            tot += n
            ans = max(ans, tot)
        return ans