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
    For this problem, we can solve this by splitting the linked list into 2 halves using the fast/slow
    pointer technique and then reverse 2nd half and then interleave the pointers together
    */
    void reorderList(ListNode* head) {
        //initialize fast/slow pointers
        ListNode* fast = head;
        ListNode* slow = head;

        //iterate fast pointer until it reaches the end of list
        while (fast && fast->next) 
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        //seperate into list1 and list2 based off of slow pointer
        ListNode* list1 = head;
        ListNode* list2 = slow->next;

        //remember to actually SPLIT them
        slow->next = nullptr;

        //reverse list2  using helper method
        list2 = reverse(list2);

        //interweave list1 and list2
        while (list1 && list2) 
        {
            //store next values for list1 and list2 to reference later
            ListNode* nxt1 = list1->next;
            ListNode* nxt2 = list2->next;

            //interweave starting from list 1
            list1->next = list2;
            list2->next = nxt1;

            //increment lists
            list1 = nxt1;
            list2 = nxt2;
        }
    }

    /*
    Helper method to reverse 2nd linked list
    */
    ListNode* reverse(ListNode* head) 
    {
        //store a reference for current and previous nodes for reversal
        ListNode* curr = head;
        ListNode* prev = nullptr;

        //iterate through current while current != nullptr
        while (curr) 
        {
            //store next pointer for temporary usage
            ListNode* nxt = curr->next;

            //update next pointer in current node
            curr->next = prev;

            //update previous pointer to be current node
            prev = curr;

            //incremenet node to next node in Linked List
            curr = nxt;
        }

        return prev;
    }
};
