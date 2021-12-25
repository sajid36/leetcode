# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    
    
        ptr = result= ListNode(0)
        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 500
                
                
            if l2:
                val2 = l2.val
            else:
                val2 = 500
                
                
            if (val1==500):
                result.next = ListNode(val2)
                l2 = l2.next
                result = result.next
            elif (val2==500):
                result.next = ListNode(val1)
                l1 = l1.next
                result = result.next
            else:
                if val1 < val2:
                    result.next = ListNode(val1)
                    l1 = l1.next
                    result = result.next
                    
                else:
                    result.next = ListNode(val2)
                    l2 = l2.next
                    result = result.next
                    
                    
        return (ptr.next)
                
            
        
        