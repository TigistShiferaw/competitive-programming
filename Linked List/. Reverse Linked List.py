class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        if head==None:
            return head
        while head!=None:
            arr.append(head)
            head=head.next
        arr=arr[::-1]        
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None 
        return arr[0]
        