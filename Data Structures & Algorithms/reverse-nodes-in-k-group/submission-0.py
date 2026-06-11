# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Yeah tbh I'm thinking we just have our previous reverse everythign in LL code but iterate over K nodes
and only reverse those specific ones tbh.

first thoughts: time to recursionmaxx
seocond thought: maybe I can get this working with nested while + iteration

Ok, I think I have the algorithm now:

1. Check if we have k nodes left
2. Identify the connection points (node after the END of the k group + node at the start of the k group (this will be tail))
3. Standard reversal of the k nodes 
4. Connect groupPrev.next to the head of the new list and connect tail of newly reversed group to groupNext
5. Shift your pointers so we can prepare groupPrev by moving forward to next group
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #use a dummy node to handle changing the k groups
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            #find the kth node from groupPrev
            kth = self.getKth(groupPrev, k)

            #if we dont have enough nodes to reverse the LL, we're done
            if not kth:
                break
            
            #save the start of the NEXT group
            groupNext = kth.next

            #now we need to do a standard reversal from current node to groupNext
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            #now we can finally stitch all the nodes back together correctly
            tmp = groupPrev.next #this was the old head but now its the tail
            groupPrev.next = kth #groupPrev now points to head
            groupPrev = tmp #update groupPrev for next iteration
        return dummy.next
    #helper method to seek the kth node
    def getKth(self, curr: Optional[ListNode], k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


