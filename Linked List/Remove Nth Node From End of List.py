class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node=start=ListNode()
        arr=[]
        while head!=None:
            arr.append(head.val)
            head=head.next
        i=0    
        while i in range(len(arr)):
            if len(arr)==n:
                i+=1
                if i<len(arr):
                    node.next= ListNode(arr[i])
                    node=node.next
            else:    
                node.next= ListNode(arr[i])
                if (i+1)==(len(arr)-n):
                    i+=1
                node=node.next
                i+=1
            
        return start.next 