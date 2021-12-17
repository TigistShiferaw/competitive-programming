class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        rearranged=[0]*len(nums)
        if (len(nums))%2==0:
            m = (len(nums)//2)-1
            for i in range(0,len(nums),2):
                rearranged[i]=nums[m]
                m-=1
            m=(len(nums)//2)-1
            for i in range(1,len(nums),2):
                rearranged[i]=nums[m+1]
                m+=1
        else:
            m = len(nums)//2
            for i in range (0,len(nums),2):
                rearranged[i] = nums[m]
                m -= 1
            m = len(nums)//2
            for i in range (1,len(nums),2):
                rearranged[i] = nums[m+1]
                m += 1
        return rearranged