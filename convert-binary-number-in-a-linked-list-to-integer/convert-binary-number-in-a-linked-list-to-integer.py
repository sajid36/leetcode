# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binList = []
        while(head!=None):
            #print(head.val)
            binList.append(head.val)
            head = head.next
            
        res = int("".join(str(x) for x in binList), 2)
        return (res)
        