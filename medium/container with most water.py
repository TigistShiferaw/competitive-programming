class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        while left<right:
            width=right-left
            height=min(height[left], height[right])
            a =width*height
            ans=max(a,ans)
            lh=height [left]
            rh=height [right]
            if   lh<rh :
                left+=1
            else:
                right-=1
        return ans
                