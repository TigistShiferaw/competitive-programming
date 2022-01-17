class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total=0
        for i in nums:
            total+=i
        def get_max(left,right,turn):
            if left==right:
                if turn==0:
                    return 0
                else:
                    return nums[left]
            if turn==1:
                return max(nums[left]+get_max(left+1,right,0),nums[right]+get_max(left,right-1,0))
            else:
                return min(get_max(left+1,right,1),get_max(left,right-1,1))
        if get_max(0,len(nums)-1,1)>=total/2:
            return True
        else:
            return False