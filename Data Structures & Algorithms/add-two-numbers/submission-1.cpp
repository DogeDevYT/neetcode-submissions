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
    Allright so for this problem I think I see a pretty straightforward solution.
    We keep iterating over every linked list node we have and keep a "carry" digit that we move
    forwards on and on until we finish both lists while keeping track of carry.
    */
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //initialize carry variable
        int carry = 0;

        //initialize return list
        ListNode* head = new ListNode(0);
        ListNode* node = head; //this is the variable we are performing operations on

        //iterate while both linked lists are non empty
        while (l1 && l2) 
        {
            //take sum of l1 and l2 val + carry as our new total
            int total = carry + l1->val + l2->val;

            //update carry and value to put into newNode
            carry = total / 10;

            //update pointers and create new node
            node->next = new ListNode(total % 10);
            node = node->next;

            //increment lls
            l1 = l1->next;
            l2 = l2->next;
        }

        //fill in remainder of whatevers left
        int total2 = 0;
        if (l1) 
        {
            while (l1) 
            {
                total2 = carry + l1->val;

                carry = total2 / 10;
                
                node->next = new ListNode(total2 % 10);

                node = node->next;
                l1 = l1->next;
            }
        } else 
        {
            while (l2) 
            {
                total2 = carry + l2->val;

                carry = total2 / 10;
                
                node->next = new ListNode(total2 % 10);

                node = node->next;
                l2 = l2->next;
            }
        }

        //in case we have carry after linked lists exhausted
        if (carry > 0) 
        {
            node->next = new ListNode(carry);
            node = node->next;
        }

        return head->next;
    }
};
