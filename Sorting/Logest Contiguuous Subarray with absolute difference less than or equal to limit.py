class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queuemax=[]
        queuemin=[]
        answer=0
        start=0
        end=0
        while end<len(nums):
            while queuemin and nums[queuemin[-1]]>=nums[end]:
                queuemin.pop()
            queuemin.append(end)
           
            while queuemax and nums[queuemax[-1]]<=nums[end]:
                queuemax.pop()
            queuemax.append(end)
            if nums[queuemax[0]]-nums[queuemin[0]]<=limit:
                answer=max(answer,end-start+1)
                end+=1
            else:
                start+=1
                if start>queuemin[0] :
                    queuemin.pop(0)
                if start>queuemax[0]:
                    queuemax.pop(0)
                
             
        return answer
                
            
            