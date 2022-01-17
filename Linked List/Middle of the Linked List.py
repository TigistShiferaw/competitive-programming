class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        k=0
        while head!=None:
            arr.append(head)
            head=head.next
        k=(len(arr)//2)
                
        return arr[k]