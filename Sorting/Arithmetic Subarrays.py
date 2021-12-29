class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolean=[]
        b=True
        for i in  range(len(r)):
            arr=[]
            for j in range(l[i],r[i]+1):
                arr.append(nums[j])
            arr.sort()
            print(i)
            print(arr)
            for j in range(1,len(arr)):
                if arr[j]-arr[j-1]==arr[1]-arr[0]:
                    b=True
                else:
                    b=False 
                    break
            boolean.append(b)
        return boolean         
                    