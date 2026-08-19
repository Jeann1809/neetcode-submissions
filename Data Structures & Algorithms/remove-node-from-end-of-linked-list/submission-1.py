# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        total = 0
        while dummy != None:
            total+=1
            dummy = dummy.next
        
        position = total-(n-1)
        current = 0

        if position == 1:
            head = head.next
            return head
        
        dummy = head
        while dummy != None:
            current+=1
        
            if current == position-1:
                prev = dummy
                after = dummy.next.next
                prev.next = after
                return head

            dummy = dummy.next
        