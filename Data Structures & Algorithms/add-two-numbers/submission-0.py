# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Allright so for this problem I think I see a pretty straightforward solution.
    We keep iterating over every linked list node we have and keep a "carry" digit that we move
    forwards on and on until we finish both lists while keeping track of carry.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #initialize our carry variable
        carry = 0

        #intialize our return list
        head = node = ListNode()

        #iterate while both linked lists are non empty
        while l1 and l2:
            #take sum of l1 and l2 val + carry as our new total to form our node
            total = carry + l1.val + l2.val
            
            #update carry and value to put into newNode
            carry = total // 10
            newNode = ListNode(total % 10)

            #update pointers
            node.next = newNode
            node = newNode

            #incrment lls
            l1 = l1.next
            l2 = l2.next
        
        #now fill in remainder of whatever list is left
        total2 = 0
        if l1:
            while l1:
                total2 = carry + l1.val

                carry = total2 // 10
                newNode = ListNode(total2 % 10)

                node.next = newNode
                node = newNode

                l1 = l1.next
        else:
            while l2:
                total2 = carry + l2.val

                carry = total2 // 10
                newNode = ListNode(total2 % 10)

                node.next = newNode
                node = newNode

                l2 = l2.next
        
        #if we run out of both linked lists finally append our remaining carry
        if carry > 0:
            newNode = ListNode(carry)
            node.next = newNode
            node = newNode
        
        #now return our solution node
        return head.next