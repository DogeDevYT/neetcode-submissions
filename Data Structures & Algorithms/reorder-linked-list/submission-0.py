# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Ok for this problem, I think we have to split the linked list into 2 halves
    for the first half we can treat it as normal and for the second we need to reverse it
    we can get to 2nd half by using fast/slow pointers technique
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        #initialize fast/slow pointers
        fast, slow = head, head

        #I think we have iterate the fast pointer until it reaches the end and when it does
        #we have effectively split our list into a midpoint with slow and slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #seperate list into list 1 and list 2 portions
        list1 = head
        list2 = slow.next

        #update list1 by adding in null pointer
        slow.next = None

        #reverse list2 for analysis later
        list2 = self.reverse(list2)

        while list1 and list2:
            #store the pointers for list1.next and list2.next
            nxt1 = list1.next
            nxt2 = list2.next

            #turns out im not interleaving right so I need to fix that
            list1.next = list2
            list2.next = nxt1

            #update list1 and list2 pointers
            list1 = nxt1
            list2 = nxt2

    """
    use this helper method to reverse the 2nd linked list
    """
    def reverse(self, head: ListNode) -> ListNode:
        #store a reference to current and previous nodes for reversal
        curr = head
        prev = None

        #iterate through list while curr != None/null
        while curr:
            #store next node for iteration
            nxt = curr.next
            
            #update next pointer in current node
            curr.next = prev

            #update previous pointer
            prev = curr

            #update current pointer to next element
            curr = nxt
        
        #we need to return prev becuase loop stops on current element
        return prev