class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv= {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def remove (self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.kv:
            self.remove(self.kv[key])
            self.insert(self.kv[key])
            return self.kv[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.remove(self.kv[key])
        self.kv[key] = Node(key,value)
        self.insert(self.kv[key])
        if len(self.kv) > self.cap:
            del self.kv[self.left.next.key]
            self.remove(self.left.next)
            
