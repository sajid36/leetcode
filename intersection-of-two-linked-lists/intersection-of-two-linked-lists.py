# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashset = set()
        
        ptr = headA
        while ptr:
            hashset.add(ptr)
            ptr = ptr.next
        
        ptr = headB
        while ptr:
            if ptr in hashset:
                return ptr
            ptr = ptr.next
        
        return None
        