class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = max(nums)
        if len(nums) < 3:
            return ans
        for i in range(3):
            if nums:
                x = max(nums)
                nums.remove(x)
                ans = min(ans, x)
        return ans