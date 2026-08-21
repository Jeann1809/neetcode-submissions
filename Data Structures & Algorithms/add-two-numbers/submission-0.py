# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        dummy1 = l1
        dummy2 = l2

        while dummy1 != None:
            arr1.append(dummy1.val)
            dummy1 = dummy1.next

        while dummy2 != None:
            arr2.append(dummy2.val)
            dummy2 = dummy2.next
        
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        result = int("".join(str(x) for x in arr1)) + int("".join(str(x) for x in arr2))
        resultarr =  [int(x) for x in str(result)]

        resultarr = resultarr[::-1]

        i = 0
        headres = ListNode(resultarr[i], None)
        current = headres

        while i < len(resultarr):
            i+=1
            if i == len(resultarr):
                current.next = None
                return headres
            else:
                newnode = ListNode(resultarr[i])
                current.next = newnode
                current = newnode      


        

         