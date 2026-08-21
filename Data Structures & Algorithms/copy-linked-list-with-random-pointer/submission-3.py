class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {None: None}
        dummy = head
        while dummy:
            hashmap[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = hashmap[dummy]
            copy.next = hashmap[dummy.next]
            copy.random = hashmap[dummy.random]
            dummy = dummy.next

        return hashmap[head]