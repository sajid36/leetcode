# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        ptr = head
        while (head):
            total = total + 1
            head = head.next
            
        total = int(total/2) + 1
        for i in range (total-1):
            ptr = ptr.next
            
        return (ptr)