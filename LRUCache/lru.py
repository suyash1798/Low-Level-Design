from LRUCache.DoublyLinkedList import DoublyLinkedList
from LRUCache.node import Node

class LRU:
    ll: DoublyLinkedList
    keyToNode: dict
    capacity: int
    count: int

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ll = DoublyLinkedList()
        self.keyToNode = {}
        self.count = 0
    
    def get(self, key: str) -> str | None:
        if key not in self.keyToNode:
            return None
        
        node = self.keyToNode[key]
        
        self.ll.remove(node)
        self.ll.addToFront(node)

        return node.value

    def add(self, key: str, value: str) -> bool:
        if key in self.keyToNode:
            return self.update(key, value)

        node = Node(key, value)

        self.keyToNode[key] = node
        self.ll.addToFront(node)
        self.count += 1

        if self.count > self.capacity:
            delNode = self.ll.removeLRU()
            del self.keyToNode[delNode.key]
            self.count -= 1

        return True

    def update(self, key: str, value: str) -> bool:
        if key not in self.keyToNode:
            return False
        
        node = self.keyToNode[key]

        node.value = value

        self.ll.remove(node)
        self.ll.addToFront(node)

        return True

    def delete(self, key: str) -> bool:
        if key not in self.keyToNode:
            return True
        
        node = self.keyToNode[key]

        del self.keyToNode[key]

        self.ll.remove(node)
        self.count -= 1

        return True
