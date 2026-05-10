class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.keys = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        self.keys.pop(node.key)
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def insert(self, node):
        self.keys[node.key] = node
        node.nxt = self.right
        node.prev = self.right.prev
        node.prev.nxt = node
        self.right.prev = node

    def get(self, key: int) -> int:
        res = -1
        if key in self.keys:
            res = self.keys[key].val
        else:
            return res
        
        self.remove(self.keys[key])
        self.insert(Node(key, res))
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.remove(self.keys[key])
        self.insert(Node(key, value))
        if len(self.keys) > self.cap:
             self.remove(self.left.nxt)
