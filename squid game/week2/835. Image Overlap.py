class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        one1 = []
        one2 = []
        
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    one1.append((i,j))
                    
                if img2[i][j] == 1:
                    one2.append((i,j))
          
        dic = {}
        ans = 0
        
        for o1 in one1:
            for o2 in one2:
                diff = (o1[0] - o2[0], o1[1] - o2[1])
                
                if diff in dic:
                    dic[diff] += 1
                else:
                    dic[diff] = 1
                ans = max(ans, dic[diff])
        return ans