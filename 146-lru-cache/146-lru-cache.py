class Node:
    def __init__(self, key, val):
        self.key, self.val = key , val
        self.prev = self.next = None
class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {} # hashmap of cache key : node
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right, self.left
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev  
       
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.lru:
            self.delete(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.delete(self.lru[key])
        self.lru[key] = Node(key, value)
        self.insert(self.lru[key])
        
        if len(self.lru) > self.capacity:
            lru_node = self.left.next
            self.delete(lru_node)
            print(lru_node in self.lru)
            del self.lru[lru_node.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)