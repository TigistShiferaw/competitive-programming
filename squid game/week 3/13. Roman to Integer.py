class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {}
        ans = 0
        symboles =["I","IV","V","VI","VII","VIII","IX","X","XL","L","LX","LXX","LXXX","XC","C","CD","D","DC","DCC","DCCC","CM","M"]
        Value = [1,4,5,6,7,8,9,10,40,50,60,70,80,90,100,400,500,600,700,800,900,1000]
        i = 0
        while i < len(symboles):
            dic[symboles[i]] = Value[i]
            i += 1
        i = 0
        while i < (len(s)):
            st = s[i]
            while st in dic and i < len(s):
                i += 1
                if i <len(s):
                    st += s[i]
               
            if st not in dic:
                sn = list(st)
                sn.pop()
                st = "".join(sn)
                i -= 1
            i += 1
            ans += dic[st]
            
        return ans