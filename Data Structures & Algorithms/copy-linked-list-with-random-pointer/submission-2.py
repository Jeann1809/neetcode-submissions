"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        copyhead = Node(head.val, None, head.random)
        prev = copyhead
        hashmap = {head:copyhead, None: None}

        dummy = head.next

        while dummy != None:
            newNode = Node(dummy.val,None,dummy.random)
            hashmap[dummy] = newNode
            prev.next = newNode
            prev = newNode
            dummy = dummy.next

        dummy = copyhead

        while dummy != None:
            dummy.random = hashmap[dummy.random]
            dummy = dummy.next

        return copyhead