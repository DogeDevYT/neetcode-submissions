# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Ok after reading up the solution algorithm I get what we need to do now:

    - We maintain a dummy node to serve as the start of our list while we repeatedly iterate over
    over linked lists
    - We maintain the pointers such that when we add a new list to our dummy node origin: we iterate
    the pointer that we added to the next node
    - When one of the lists is empty, add the remaining one as the next element
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            #list 1s current value since its <=
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                #list 2 is current value since its >
                node.next = list2
                list2 = list2.next
            #dont forget to iterate to the next node
            node = node.next
        
        #assign remainder of list to whatevers left
        node.next = list1 or list2

        #return dummy node for combined linked lists
        return dummy.next