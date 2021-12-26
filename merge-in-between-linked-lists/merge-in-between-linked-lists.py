# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        firstCut = None
        lastPart = None
        counter = -1
        while list1:
            counter = counter + 1
            if counter == a:
                if(a==b):
                    firstCut = prev
                    lastPart = list1.next
                    list1 = list1.next 
                else:
                    firstCut = prev
                    list1 = list1.next
            elif counter == b:
                lastPart = list1.next
                list1 = list1.next
            else:
                prev = list1
                list1 = list1.next
                
        while list2:
            firstCut.next = list2
            firstCut = firstCut.next
            list2 = list2.next
        
        firstCut.next = lastPart
        return (ptr)
        