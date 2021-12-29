"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        ptr = Node(0)
        current, stack = ptr, [head]
        
        
        while stack:
            tmp = stack.pop()
            if tmp.next:
                stack.append(tmp.next)
            if tmp.child:
                stack.append(tmp.child)
                
            current.next = tmp
            tmp.prev = current
            tmp.child = None
            current = current.next
            
            
            
        ptr.next.prev=None
        return ptr.next
                
            
            
        