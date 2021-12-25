# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        res = []
        result=ptr=ListNode(0)
        while(head):
            if head.val not in res:
                res.append(head.val)
                result.next = ListNode(head.val)
                result=result.next
            head=head.next
            
            
                
        #print(ptr.next)
        return (ptr.next)
        