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
    Ok after reading the 2 pointer solution with first and second
    it makes a lot more sense becuase then we can just keep the 
    first pointer n steps ahead of the second so we can stop when
    first == Null and remove the node at second
    */
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode* second = head;

        int idx = 0;

        //keep prev and next pointers to track
        ListNode* prev = nullptr;
        ListNode* nxt = nullptr;

        //iterate only first until it reaches n, then iterate both
        //uintil first reaches end
        while (first) 
        {
            if (idx >= n) 
            {
                prev = second;
                second = second->next;
            }

            //we always need to set nxt to second->next regardless
            //if we're moving second or not to prevent hanging pointer
            //for later
            nxt = second->next;

            //iterate first
            first = first->next;

            //increment index
            idx++;
        }

        //now we need to prune the node at second

        //return value
        ListNode* ret = nullptr;

        //edge case - prev DNE
        if (!prev) 
        {
            ret = nxt; //start at next
        } else 
        {
            prev->next = nxt;
            ret = head;
        }
        return ret;
    }
};
