class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        i=0
        for j in range(len(nums)):
            k+=nums[j]
            while k<(nums[j]*(j-i+1)):
                k-=nums[i]
                i+=1
            ans=max(ans,j-i+1)
        return ans
                
                
                