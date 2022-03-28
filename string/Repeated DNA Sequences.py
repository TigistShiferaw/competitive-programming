class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        j=0
        exist=set()
        string=""
        ans=[]
        while j<len(s):
            if len(string)==10:
                string=string[1:]
            for m in range(len(string),10):
                if j<len(s):
                    string+=s[j]
                j+=1
            if string in exist:
                ans.append(string)
            else:
                if len(string)==10:
                    exist.add(string)
        vis=set() 
        res=[]
        for i in range(len(ans)):
            if ans[i] not in vis:
                
                res.append(ans[i])
                vis.add(ans[i])
            else:
                vis.add(ans[i])
           
        return res