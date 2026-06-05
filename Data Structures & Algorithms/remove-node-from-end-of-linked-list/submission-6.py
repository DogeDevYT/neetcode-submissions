# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Ok after reading the 2 pointer solution with first and second
    it makes a lot more sense becuase then we can just keep the 
    first pointer n steps ahead of the second so we can stop when
    first == Null and remove the node at second
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize our first/second pointers
        first, second = head, head

        idx = 0

        #keep prev and next pointers to track
        prev = None
        nxt = None

        #iterate only first until it reaches n, then iterate both
        #until first reaches end
        while first:
            if idx >= n:
                prev = second
                second = second.next

            #we need to always set next pointer to second.next
            #because otherwise we get dangling pointers
            nxt = second.next
            
            #iterate first always
            first = first.next

            #iterate index to track
            idx += 1
        #prune the node

        #return value
        ret = None
        
        #edge case - prev DNE
        if not prev:
            ret = nxt
        else:
            prev.next = nxt
            ret = head
        return ret
