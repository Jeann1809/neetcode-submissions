class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return
        else:
            if len(self.cache) == self.capacity:
                lnode = self.left.next
                del self.cache[lnode.key]
                self.remove(lnode)
                node = Node(key,value)
                self.cache[key] = node
                self.insert(node)
            else:
                node = Node(key,value)
                self.cache[key] = node
                self.insert(node)



    def insert(self, node:Node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        return

    def remove(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return


    
        
