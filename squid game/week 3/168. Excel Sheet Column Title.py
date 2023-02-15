class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        num = columnNumber
        ans = []
        cnt = 2
        while num > 0:
            num -= 1
            ans.append(chr(65 +(num % 26)))
            num //= 26 

        ans.reverse()
        ans = "".join(ans)
        return ans