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
    yeah so for this one I was thinking we have 2 pointers: fast and slow.

    Basically we're guarenteed that if our slow pointer moves one step at a time
    and our fast pointer moves 2 steps at a time, the fast one will have to be intersecting the slow
    one at one stop, given that there is a cycle, otherwise the fast one will get to the end and the loop 
    will finish early
    */
    bool hasCycle(ListNode* head) {
        //initialize pointers
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast && fast->next) 
        {
            fast = fast->next->next;
            slow = slow->next;

            if (fast == slow) return true;
        }

        return false;
    }
};
