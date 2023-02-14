class Solution:
    def minimumDeletions(self, s: str) -> int:
        bPrefix = [0] * len(s)
        aSuffix = [0] * len(s)
        if s[0] == "b":
            bPrefix[0] = 1
        if s[-1] == "a":
            aSuffix[-1] = 1
        
        for i in range(1,len(s)):
            if s[i] == "b":
                bPrefix[i]  = bPrefix[i-1] + 1
            else:
                bPrefix[i] = bPrefix[i - 1]
        for i  in range(len(s) - 2, -1, -1):
            if s[i] == "a":
                aSuffix[i]  = aSuffix[i + 1] + 1
            else:
                aSuffix[i] = aSuffix[i + 1]
        ans = inf
        for i in range(len(s)):
            ans = min (ans, aSuffix[i] + bPrefix[i] - 1)
        return ans
