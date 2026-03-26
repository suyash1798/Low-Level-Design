from LRUCache.node import Node

class DoublyLinkedList:
    head: Node
    tail: Node
    count: int

    def __init__(self):
        self.head = Node('dummy', 'dummy')
        self.tail = Node('dummy', 'dummy')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def addToFront(self, node: Node) -> bool:
        if node == None:
            return False

        nxt = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nxt
        nxt.prev = node

        self.count += 1

        return True
    
    def remove(self, node: Node) -> bool:
        if node == None or node.prev == None or node.next == None:
            return True # Even if its not there end goal achieved
        
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        node.prev = None
        node.next = None

        self.count -= 1

        return True
    
    def removeLRU(self) -> Node | None:
        if self.count == 0:
            return None
        
        node = self.tail.prev
        prev = node.prev
        # unlink node (which is the last real node before tail)
        prev.next = self.tail
        self.tail.prev = prev

        node.next = None
        node.prev = None

        # decrement count to reflect removal
        self.count -= 1

        return node
