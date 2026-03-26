from LRUCache.lru import LRU

lru = LRU(2)

if lru.add('1', 'hello') == True:
    print('Added')
if lru.add('2', 'world') == True:
    print('Added')
lru.delete('2')
if lru.add('3', '!') == True:
    print('Added')

print(lru.get('1'))
print(lru.get('2'))
print(lru.get('3'))
    
        


    