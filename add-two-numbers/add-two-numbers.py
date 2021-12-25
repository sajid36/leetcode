# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = l1
        ll2 = l2
        carry = 0
        flag, flag2 = 0,0
        ptr = result = ListNode(0)
        while True: 
            if (flag==1 and flag2==1):
                break
            
            if ll1:
                val1 = ll1.val
                ll1 = ll1.next
                
            else:
                val1 = 0
                flag = 1
                
            if ll2:
                val2 = ll2.val
                ll2 = ll2.next
                
            else:
                val2 = 0
                flag2 = 1
                
            if(flag!=1 or flag2!=1):    
                total = carry + val1 + val2
                #print(total)

                result.next = ListNode(total%10)
                carry = int(total/10)
                result = result.next
            
        if carry > 0:
            result.next = ListNode(carry) 
            
        return ptr.next