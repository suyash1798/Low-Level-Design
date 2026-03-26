Requirements

1. User able to save a key
2. User able to retrive a saved key
3. User able to update a key
3. System should evict least recently used key in case of no space
4. All operations should be in O(1)


Entities

1. Doubly linklist Queue
   - head
   - tail
   - count
   - addNode
   - deleteNode
   - getNode
   - getCount
2. Node
   - key
   - value
   - prev
   - next
3. LRU
   - list
   - map(key, node)
   - size
   - addKey
   - deleteKey
   - updateKey
   - getSize
   - getCapacity