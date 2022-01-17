class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""
        arr=[]
        while l1!=None:
            num1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            num2+=str(l2.val)
            l2=l2.next
        diff=abs(len(num1)-len(num2))  
        num1=num1[::-1]
        num2=num2[::-1]
        if diff>0:
            if len (num1)>len(num2):
                num2=diff*"0"+num2
            elif len(num1)<len(num2):
                num1=diff*"0"+num1
        su=int(num1)+int(num2)     
        su=str(su)
        for i in su:
             arr.append(int(i))
       
        arr=arr[::-1]
        node=start=ListNode()
        for i in range(len(arr)):
            node.next=ListNode(arr[i])
            node=node.next
        
        return start.next    