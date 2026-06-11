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

#include <vector>

/*
Ok, this problem shouldn't be too difficult, all we have to do is
merge sort the 2 LLs by using our previous soluition for merging 2 smaller
LLs as a helper function
*/
class Solution {
private:
    //helper function to merge 2 sorted LLs
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) 
    {
        ListNode* dummy = new ListNode(0);
        ListNode* node = dummy; //reference dummy for operations

        //while both lists valid ierate on both and merge
        while (l1 && l2) 
        {
            if (l1->val <= l2->val) 
            {
                node->next = l1;
                l1 = l1->next;
            } else 
            {
                node->next = l2;
                l2 = l2->next;
            }

            //iterate node regardless
            node = node->next;
        }

        //add back remainder
        if (l1) 
        {
            node->next = l1;
        } else if (l2) 
        {
            node->next = l2;
        }

        //return the finished list
        return dummy->next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //account for edge case where we have no lists
        if (lists.empty()) return nullptr;

        //iterate over merging the lists until the length is <2
        while (lists.size() > 1) 
        {
            //create a temp array to store this step of lists being merged
            std::vector<ListNode*> merged_lists;

            //iterate in twos
            for (int i = 0; i < lists.size(); i += 2) 
            {
                //store current and next list pointers to merge
                ListNode* curr = lists[i];

                ListNode* nxt = nullptr;
                //if we have a list node, add it to our merged lists
                //otherwise just use a nullptr
                if ((i+1) < lists.size()) 
                {
                    nxt = lists[i + 1];
                }

                //append our combined lists to merged lists
                merged_lists.push_back(mergeTwoLists(curr, nxt));
            }

            lists = merged_lists; //reset pointer to point to new merged lists
        }

        return lists[0];
    }
};
