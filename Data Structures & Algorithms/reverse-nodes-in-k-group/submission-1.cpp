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

/*
Ok, I think I have the algorithm now:

1. Check if we have k nodes left
2. Identify the connection points (node after the END of the k group + node at the start of the k group (this will be tail))
3. Standard reversal of the k nodes 
4. Connect groupPrev.next to the head of the new list and connect tail of newly reversed group to groupNext
5. Shift your pointers so we can prepare groupPrev by moving forward to next group
*/

class Solution {
private:
    //helper method to seek the kth node
    ListNode* getKth(ListNode* curr, int k) 
    {
        while (curr && k > 0) 
        {
            curr = curr->next;
            k -= 1;
        }
        return curr;
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        //use a dummy node to handle changing the k groups
        ListNode* dummy = new ListNode(0, head);
        ListNode* groupPrev = dummy;

        //this is going to be hte main loop of the algorithm where we do a majority of all hte work
        while (true) 
        {
            //find the kth node from groupPrev
            ListNode* kth = getKth(groupPrev, k);

            //if we dont have enough nodes to reverse the LL, we're done
            if (!kth) break;

            //now we need to save the start of the NEXT group
            ListNode* groupNext = kth->next;

            //now we need to do a standard reversal from current node to group next
            ListNode* prev = kth->next;
            ListNode* curr = groupPrev->next;

            while (curr != groupNext) 
            {
                ListNode* nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }

            //now we can finally stitch all the nodes back together correctly this time.
            ListNode* tmp = groupPrev->next; //this used to be the old head but now its the tail
            groupPrev->next = kth; //groupPrev now points to the new head
            groupPrev = tmp; //update groupPrev to be the tail
        }

        return dummy->next;
    }
};
