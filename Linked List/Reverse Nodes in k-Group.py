class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array=[]
        arr=[]
        ans=[]
        node=start=ListNode()
        he=head
        while he!=None:
            array.append(he.val)
            he=he.next
        j=0
        while j in range(len(array)):
            arr=[]
            i=1
            m=j 
            while i<=k and m<len(array) :
                arr.append(array[m])
                i+=1
                m+=1
            if len(arr)==k:
                arr=arr[::-1]
            for b in range(len(arr)):
                ans.append(arr[b])   
            j+=k
        for i in ans:
            node.next=ListNode(i)
            node=node.next
        return start.next
                