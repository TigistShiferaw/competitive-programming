class Solution: 
    def select(self, arr, i):
        # code here
        min=arr[i]
        index=i
        for j in range(i+1,len(arr)):
            
            if arr[j]<min:
                min=arr[j]
                index=j
        return min,index        
        
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            
            min,index=self.select(arr,i)
            temp=arr[i]
            arr[index]=temp
            arr[i]=min
        return arr  