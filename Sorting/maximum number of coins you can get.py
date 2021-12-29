class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        selected=[]
        maxIhave=0
        for i in range((len(piles)//3)):
            selected=[]
            if len(piles)!=0:
                selected.append(piles.pop(-1))
                selected.append(piles.pop(-1))
                selected.append(piles.pop(0))
            selected.pop(0)    
            maxIhave+=max(selected)
        return maxIhave   