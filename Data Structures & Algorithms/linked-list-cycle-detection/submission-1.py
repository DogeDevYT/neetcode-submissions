# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Tbh I was thinking we use more Hashmap Slop to keep track of seen nodes and add nodes that we haven't seen
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Create a hash SET instead of hash map to make it FAR easier on ourselves
        slop = set()

        curr = head

        #progressively more more and more
        while curr:
            if curr in slop:
                return True
            else:
                slop.add(curr)
            curr = curr.next
        return False