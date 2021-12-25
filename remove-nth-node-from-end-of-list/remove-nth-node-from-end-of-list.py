# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        index = 0
        while (temp):
            temp = temp.next
            index = index + 1
        
        if index == 1:
            return None
        x=index-n  
        if x==0:return head.next
        
        temp = head
        temp2 = head
        counter = 0
        while(counter!=x):
            temp = temp2
            temp2 = temp2.next
            counter = counter + 1
            
        temp.next = temp2.next
        return (head)
            
            
        
        