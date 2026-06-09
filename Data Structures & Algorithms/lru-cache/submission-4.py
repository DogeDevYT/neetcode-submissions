"""
To be honest, on first glance, this problem seems like hashmap slop but lets code it in and see what happens

We're going to use a hashmap here to encode all results and get them back in constant time

UPDATE: After thinkign about it fo ra bit I remembered that we can use a doubly linked list to store MRU elements
at tail and LRU elements at head

UPDATE: I had to start over this problem takes a while but at least I have the right idea now
"""
class ListNode:
    def __init__(self, nkey: int,  nval: int):
        self.key = nkey
        self.val = nval
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #my mistake earlier was just having this be key:value when it should've been key:ListNode
        #for constant access time

        #fix our dummy boundaries on LRU cache to be just head and tail pointing to each other
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node: ListNode):
        #this isolates a node by changing around pointers so that its neighbors are together
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def _add_to_tail(self, node: ListNode):
        #insert node right before dummy tail
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node   
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            #move to tail since its most recently used
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value #update value
            self._remove(node) #move to tail
            self._add_to_tail(node)
            return #early return

        #add node if its not already in cache
        sonion = ListNode(key, value)
        self.cache[key] = sonion
        self._add_to_tail(sonion)

        #remove if over cache size
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
