class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        stack=[]
        count=0
        nums.sort()
        for i in range(len(nums)):
            if stack and stack[-1]>=nums[i]:
                count+=(stack[-1]-nums[i])+1
                stack.append(nums[i]+((stack[-1]-nums[i])+1))
                
            else:
                stack.append(nums[i])
        print(stack)       
        return count