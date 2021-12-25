# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_head = head 
        fast_head = head
        while slow_head and fast_head and fast_head.next and fast_head.next.next:
            slow_head = slow_head.next
            fast_head = fast_head.next.next
            if slow_head == fast_head:
                return True
        return False
        