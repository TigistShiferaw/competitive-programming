class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair=[]
        pairs=[]
        nums.sort()
        sumofPairs=[]
        minMaxsum=0
        for i in range(len(nums)//2):
            if len(nums)!=0:
                pair=[]
                pair.append(nums.pop(-1))
                pair.append(nums.pop(0))
                pairs.append(pair)
        for i in range(len(pairs)):
            sumofPairs.append(pairs[i][0]+pairs[i][1])
        minMaxsum=max(pairs)[0]+max(pairs)[1]   
        return max(sumofPairs)
        