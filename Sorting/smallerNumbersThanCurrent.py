class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countArr=[0]*(len(nums))
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    countArr[i]=countArr[i]+1
        return countArr