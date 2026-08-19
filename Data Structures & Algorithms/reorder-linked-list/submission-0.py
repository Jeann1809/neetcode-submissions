# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        [0, 1, 2, 3, 4, 5, 6]
        
        1. Transform the linked list into an array
        2. Divide the array into two sections
        3. set left and right pointer 
        4. Keep reducing the pointers l++ and r--
        5. For each time change the value in the linkedd list 

        [0, 6, 1, 5, 2, 4, 3]
        '''
        dummy = head
        arr = []
        while dummy != None:
            arr.append(dummy.val)
            dummy = dummy.next
        
        l,r = 0,len(arr)-1
        dummy = head
        while l < r:
            dummy.val = arr[l]
            dummy = dummy.next
            dummy.val = arr[r]
            dummy = dummy.next
            l+=1
            r-=1
        
        if l == r:
            dummy.val = arr[l]
        

        