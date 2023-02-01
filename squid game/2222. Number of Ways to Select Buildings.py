class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix_0 = [0] * len(s)
        suffix_0 = [0] * len(s)
        prefix_1 = [0] * len(s)
        suffix_1 = [0] * len(s)

        for i in range(len(s)):
            if s[i] == "1":
                if i > 0:
                    prefix_1[i] = 1 + prefix_1[i - 1]
                else:
                    prefix_1[i] = 1
            elif i > 0:
                prefix_1[i] = prefix_1[i - 1]
            if s[i] == "0":
                if i > 0:
                    prefix_0[i] = 1 + prefix_0[i - 1]
                else:
                    prefix_0[i] = 1
            elif i > 0:
                prefix_0[i] = prefix_0[i - 1]
        for i in range(len(s) - 1, -1, -1):
            # print(s[i])
            if s[i] == "1":
                if i < (len(s) - 1):
                    suffix_1[i] = 1 + suffix_1[i + 1]
                else:
                    suffix_1[i] = 1
            elif i < len(s) - 1:
                suffix_1[i] = suffix_1[i  + 1]
            if s[i] == "0":
                if i < len(s) - 1:
                    suffix_0[i] = 1 + suffix_0[i + 1]
                else:
                    suffix_0[i] = 1
            elif i < len(s) - 1:
                suffix_0[i] = suffix_0[i  + 1]
            ans = 0
       
        for i in range(len(s)):
            if s[i] == "0":
                ans += prefix_1[i] * suffix_1[i]
            else:
                ans += prefix_0[i] * suffix_0[i]
        return ans

            