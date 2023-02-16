class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dic = {}
        changed.sort()
        if len(changed) %2 != 0:
            return []
        for i in range(len(changed)):
            if changed[i] in dic:
                dic[changed[i]] += 1
            else:
                dic[changed[i]] = 1
                
        ans = []
        chan = set(changed)
        vis = set()
        for c in changed:
            x = 2 * c
            if x in chan and x not in vis and c not in vis and not (dic[c] ==1 and x == c):
                ans.append(c)
                dic[x] -= 1
                dic[c] -= 1
                if dic[x] == 0:
                    vis.add(x)
                    chan.remove(x)
                if dic[c] == 0:
                    vis.add(c)
                    if c in chan:
                        chan.remove(c)
        
        # print(ans)
        if len(ans) == len(changed)//2:
            return ans
        return []