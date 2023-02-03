class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        dic1 = defaultdict(list)
        queue = deque()
        queue.append((root,0,0,0))
        while queue:
            q,r,c,level = queue.pop()
            if q:
                dic1[(r,c,level)].append(q.val)
                queue.append((q.left, r + 1, c - 1,level + 1))
                queue.append((q.right, r + 1, c + 1,level + 1))
        for d in dic1:
            dic1[d].sort()
        index = sorted(dic1.keys(), key = lambda x:x[2])
        dic2 = defaultdict(list)
        for i in index:
            dic2[i[1]] += dic1[i]
        
        ans = sorted(dic2.keys())
        res = []
        for a in ans:
            res.append(dic2[a])
        return res
