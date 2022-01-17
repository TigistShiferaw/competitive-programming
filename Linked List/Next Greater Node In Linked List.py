class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        arr=[]
        stack=[]
        while head!=None:
                arr.append(head.val)
                head=head.next 
        soln=[0]*len(arr)        
        for i in range(len(arr)):
            if stack:
                if stack[-1][0]>=arr[i]:
                    stack.append((arr[i],i))
                else:
                    while stack and stack[-1][0]<arr[i]:
                        soln[stack[-1][1]]=arr[i]
                        stack.pop()
                    stack.append((arr[i],i))    
            else:
                stack.append((arr[i],i))
                
        return soln   
        