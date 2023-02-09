class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        def rec(i, path,st):
            if i >= len(s):
                if len(path) == 4:
                    ans.append(path.copy())
                return 
            st += s[i]
            take = None
            if len(str(int(st))) == len(st)  and int (st) <= 255:
                take = rec(i + 1, path + [st],"")
            notTake = rec(i + 1, path,st)
            return
        rec(0, [],"")
        res = []
        for a in ans:
            temp = ""
            cnt = 0
            for i in range(len(a)):
                temp += a[i]
                cnt += len(a[i])
                if i < len(a) -1:
                    temp += "."
            # print(cnt,len(s))
            if cnt == len(s):
                res.append(temp)
        return res