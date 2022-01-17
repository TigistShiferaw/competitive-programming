class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length=(2**n)-1
        middle=(length//2)+1
        
        if n==1:
            return "0"
        if k==middle:
            return "1"
        if k<middle:
            return self.findKthBit(n-1,k)
        else:
            val= self.findKthBit(n-1,length-k+1)
            if val=="0":
                return "1"
            else:
                return "0"
       
    