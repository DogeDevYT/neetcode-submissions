"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Ok so from what I'm reading in the hints, we can't directly iterate over everything so we have to 
    store all nodes in a map
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #quick early return for empty LL
        if not head:
            return None

        #store a hashmap with the map of old node to new deep copied node
        # old node: deep copied node
        deepCopyMap = {}
        
        #in our first pass, we have to clone the elements straight up
        curr = head

        while curr:
            deepCopyMap[curr] = Node(curr.val)
            curr = curr.next
        
        #now that we have all elements cloned we can copy over next pointers and random
        #pointers
        curr = head
        
        while curr:
            #we store a copy of the next node by referencing our deep copy map
            #use .get as a Null check basically
            deepCopyMap[curr].next = deepCopyMap.get(curr.next)

            #do the same for random
            deepCopyMap[curr].random = deepCopyMap.get(curr.random)

            curr = curr.next
        
        return deepCopyMap[head]

