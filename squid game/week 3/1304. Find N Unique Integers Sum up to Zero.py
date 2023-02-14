class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n // 2):
            ans.append(i + 1)
            ans.append(-(i  + 1))
        if len(ans) < n:
            ans.append(0)
        return ans