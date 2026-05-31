/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:

    /*
    Ok after reading up the solution algorithm I get what we need to do now:

    - We maintain a dummy node to serve as the start of our list while we repeatedly iterate over
    over linked lists
    - We maintain the pointers such that when we add a new list to our dummy node origin: we iterate
    the pointer that we added to the next node
    - When one of the lists is empty, add the remaining one as the next element
    */
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //Ok got the issue, before I was instantiating a completely undefined node
        //we can fix this by using our constructor
        ListNode dummy(0);

        ListNode* node = &dummy;

        while (list1 && list2) 
        {
            //list 1s current value since its <= the other
            if (list1->val <= list2->val) 
            {
                node->next = list1;
                list1 = list1->next;
            } else 
            {
                //list 2s current value since its >
                node->next = list2;
                list2 = list2->next;
            }
            //dont forget to iterate
            node = node->next;
        }

        //assign whatevers left to node.next
        if (list1) node->next = list1;
        if (list2) node->next = list2;

        //return dummy
        return dummy.next;
    }
};
