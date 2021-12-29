import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic={}
        co=0
        count=0
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        d=dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
       
        if co<=len(arr)//2:
            for i in d:
                if co<len(arr)//2:
                    co+=d[i]
                    count+=1         
        
        return count
        