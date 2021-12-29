class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k=len(arr)-1
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            m=i
            for j in range(i):
                if max(arr[0:i+1])==arr[j]:
                    m=j
            if i != m:        
                ans.append(m+1)
                arr=rev(0,m,arr)
                arr=rev(0,i,arr)
                ans.append(i+1)
                
        return ans
        
def rev(start,end,arr):
        start=start
        end=end
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        return arr  
            
            