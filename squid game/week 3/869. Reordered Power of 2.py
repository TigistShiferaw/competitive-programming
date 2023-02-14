import math
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        num = str(n)
        dic1 = {}
        for s in num:
            if s in dic1:
                dic1[s] += 1
            else:
                dic1[s] = 1
            
        vis = []
        
        for i in range(int(math.log(10**9,2)) + 1):
            vis.append(str(2**i))
            
        for v in vis:
            dic2 = {}
            for i in range(len(v)):
                if v[i] in dic2:
                    dic2[v[i]] += 1
                else:
                    dic2[v[i]] = 1
            p = True
            # for d in dic1:
            #     if d not in dic2 or dic1[d] != dic2[d]:
            #         p = False
            #         continue
            if dic1 == dic2:
                return True
        
        return False
            