# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
yeah so for this one I was thinking we have 2 pointers: fast and slow.

Basically we're guarenteed that if our slow pointer moves one step at a time
and our fast pointer moves 2 steps at a time, the fast one will have to be intersecting the slow
one at one stop, given that there is a cycle, otherwise the fast one will get to the end and the loop 
will finish early
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #initialize the pointers
        fast, slow = head, head

        #repeat while fast node and next node after fast != null
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False