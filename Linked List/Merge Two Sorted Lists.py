class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Node=start= ListNode()
        arr1=[]
        arr2=[]
        arr=[]
        while list1!=None :
            arr1.append(list1.val)
            list1=list1.next
        while list2!=None:
            arr2.append(list2.val)
            list2=list2.next
        for i in arr1:
            arr.append(i)
        for i in arr2:
            arr.append(i)
        arr.sort()
        for i in arr:
            Node.next=ListNode(i)
            Node=Node.next
        return start.next    
            