# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next #refernce rest of list
            curr.next = prev #assign previous node

            prev = curr
            curr = nxt
        
        #curr will be None by now
        return prev
        