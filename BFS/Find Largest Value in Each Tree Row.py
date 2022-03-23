# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        queue=deque()
        queue.append(root)
        visited=set()
        #visited.add(root)
        ans=[]
        size=len(queue)
        while queue:
            heap=[]
            
            for s in range(size):
                x=queue.popleft()
                if x not in visited and x :
                    visited.add(x)
                    queue.append(x.left)
                    queue.append(x.right)
                    heappush(heap,-x.val)
            if len(heap)>0:
                ans.append(-heap[0])        
            size=len(queue)
        return ans    
                
                    
                    
                    
        