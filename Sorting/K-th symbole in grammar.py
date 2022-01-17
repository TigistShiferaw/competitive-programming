class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
            half=pow(2,n-2)
            
            if n==1:
                return 0
            if k<=half:
                return self.kthGrammar(n-1,k)
            else:
                value=self.kthGrammar(n-1,k-half)
                if value==0:
                    return 1
                else:
                    return 0
        
       