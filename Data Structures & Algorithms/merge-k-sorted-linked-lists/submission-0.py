# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Ok heres the lay down, I think we just need to use a subset of binary search
specifically the merge sort so we can get this working. 
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #account for edge case of empty list
        if not lists:
            return None

        #repeat merging until theres only one list left
        while len(lists) > 1:
            #use this to store the working merged lists
            merged_lists = []

            #iterate in groups of 2 so we can reference previous element
            for i in range(0, len(lists), 2):
                prev = lists[i]
                curr = []
                #handle edge case with odd numbered list
                if i + 1 < len(lists):
                    curr = lists[i+1]
                else:
                    curr = None

                #merge the current and previous LL and then put it in our 
                #merged 
                merged_lists.append(self.mergeTwoLists(prev, curr))
            #repeat this merging with newly paired lists
            lists = merged_lists
        return lists[0]
    
    #lets build our helper method to merge 2 LLs in sorted order then
    #in O(n)
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to append everything 2 and return head
        dummy = node = ListNode(0)

        #iterate over the 2 lists while they're still valid
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next  = l2
                l2 = l2.next
            
            #dont forget to iterate pointers
            node = node.next

        #pack up remainder of list
        if l1:
            node.next = l1
        elif l2:
            node.next = l2

        #return the rest of our list
        return dummy.next
        
