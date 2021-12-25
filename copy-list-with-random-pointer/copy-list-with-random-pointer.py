"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping = {None:None}
        
        temp = head
        while temp:
            mapping[temp] = Node(temp.val)
            temp = temp.next
        

        temp = head
        while temp:
            copy = mapping[temp]
            copy.next = mapping[temp.next]
            copy.random = mapping[temp.random]
            temp = temp.next
            
        return mapping[head]