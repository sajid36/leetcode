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
        
        res = {}
        while(head):
            if head.val not in res.keys():
                res[head.val] = 1
            else:
                res[head.val] = res[head.val] + 1
            head=head.next
            
        result=ptr=ListNode(0)
        for key,val in res.items():
            if val==1:
                result.next=ListNode(key)
                result=result.next
                
        #print(ptr.next)
        return (ptr.next)
                
                