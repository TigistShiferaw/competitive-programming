class Solution:
    def myPow(self, x: float, n: int) -> float:
        current=0
        y=n//2
        if n==0:
            return 1
        if y>=0:
            if n==1:
                return x
            current=self.myPow(x,y)
        else:
            if n==-1:
                return 1/x
            current=self.myPow(x,y)
        if n%2==0:
            return current*current
        else:
            return current*current*x
                  