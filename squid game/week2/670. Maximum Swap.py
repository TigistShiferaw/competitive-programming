class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num

        strNum = list(str(num))
        copy = strNum.copy()
        for i in range(len(strNum)):
            for j in range(len(strNum)):
                copy[i], copy[j] = copy[j], copy[i]
                nm = "".join(copy)
                nm = int(nm)
                ans = max(ans,nm)
                copy = strNum.copy()
        return ans