class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        dic={}
        count=0
        ans=[]
        node=start=ListNode()
        while head!=None:
            arr.append(head.val)
            head=head.next
        arr.sort()    
        for i in arr:
            if i in dic:
                count+=1
            else:
                count=1
            dic[i]=count
        for i in dic:
            ans.append(i)
        for i in ans:
            node.next=ListNode(i)
            node=node.next
            
        return start.next