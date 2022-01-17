class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=""
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                st1=""
                st2=""
                st1+=str(nums[i])
                st1+=str(nums[j])
                st2+=str(nums[j])
                st2+=str(nums[i])
                if int(st1)<int(st2):
                    nums[i],nums[j]=nums[j],nums[i]
        for i in nums:
            ans+=str(i)
        if int(ans)==0:
            return "0"
        return ans    
                
            