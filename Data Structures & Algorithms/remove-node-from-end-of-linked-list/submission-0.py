# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Ok I have a much better naive approach here. 

    We iterate to the end to get total length and then subtract n to get there
    while doing all this we iterate forwards again, keeping track of 
    previous/next and then basically prune out the item
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        #get total length
        curr = head

        while curr:
            curr = curr.next
            length += 1
        
        #iterate to length - n
        delta = length - n
        print(str(delta))

        idx = 0

        #store pointers
        prev = None
        curr = head
        nxt = None
        if curr:
            nxt = curr.next

        while idx < delta:
            print("Before idx: " + str(idx))
            print("Before node: " + str(curr.val))
            idx += 1
            prev = curr
            curr = nxt
            if curr.next:
                nxt = nxt.next
            else:
                nxt = None
            print("After idx: " + str(idx))
            print("After node: " + str(curr.val))
        
        #prune specific node by removing it

        #new head to return
        ret = None

        #edge case, no prev
        if not prev:
            ret = nxt
        else:
            #prune curr node
            prev.next = nxt
            print("Pruned node: " + str(curr.val))
            ret = head
        
        return ret