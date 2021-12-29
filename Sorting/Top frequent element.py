class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution=[]
        count={}
        arr=[[]for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        d=dict(sorted(count.items(), key=lambda item: item[1]))
        for i in d:
            arr.append(i)
        for i in range(k-1,-1,-1):
            solution.append(arr[-1-i])
        return solution