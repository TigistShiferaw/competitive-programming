class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        kthLargest=""
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort(reverse=True)
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range((len(nums))):
            if k==i+1:
                kthLargest=nums[i]
        return kthLargest