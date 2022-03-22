class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].append(i)
            else:
                dic[s[i]]=[i]
        ans=[]
        for c in dic:
            dic[c].sort()
        letter=s[0] 
        cnt=1
        visited=set()
        for i in range(len(s)):
            if dic[s[i]][0]<=dic[letter][-1] and s[i] not in visited:
                visited.add(s[i])
                cnt+=len(dic[s[i]])
                if dic[s[i]][-1]>dic[letter][-1]:
                    letter=s[i]  
            elif s[i] not in visited:
                if cnt>1:
                    ans.append(cnt-1)
                else:    
                    ans.append(cnt)
                letter=s[i]
                cnt=1
        else: 
            if cnt>1:
                ans.append(cnt-1) 
            else:
                ans.append(cnt)
        return ans
            
            
            
        
            
            
        
