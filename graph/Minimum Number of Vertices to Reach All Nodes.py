class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vis =set()
        ans =[]
        for i in range(len(edges)):
            if edges[i][1] not in vis:
                vis.add(edges[i][1])
        for i in range(n):
            if i not in vis:
                ans.append(i)
        return ans
                
            