# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        forward = []
        temp = head
        
        while (temp):
            forward.append(temp.val)
            temp = temp.next
            
            
        print(forward)
            
        n = len(forward) - 1
        if len(forward)%2 == 0:
            length = int(len(forward)/2)
            print(length)
            
        else:
            length = int(len(forward)/2) + 1
            print(length)
            
            
        for i in range(length):
            head.val = forward[i]
            head = head.next
            if i!=n-i:
                head.val = forward[n - i]
                head = head.next
            