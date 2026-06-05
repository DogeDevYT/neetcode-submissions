/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

#include <unordered_map>

class Solution {
public:
    /*
    Yeah I think this problem was really crazy since I have zero intution for how to go about this
    but I think the idea is we need to use a hash map to store old node : new node pairs for the LL

    We can solve this with 2 passes: 1st pass to assign nodes to our Hashmap and 2nd pass to connect
    next and random pointers
    */
    Node* copyRandomList(Node* head) {
        //quick return for empty LL
        if (!head) return nullptr;

        //hashmap
        std::unordered_map<Node*, Node*> deepCopyMap;

        //create explicit base case to handle nullptr
        deepCopyMap[nullptr] = nullptr;

        //1st pass - clone elements
        Node* curr = head;

        while (curr) 
        {
            //prevent dangling pointer by using constructor rather than referencing stack
            deepCopyMap[curr] = new Node(curr->val);

            curr = curr->next;
        }

        //2nd pass - copy over next pointers and random pointers
        curr = head;

        while (curr) 
        {
            //store a copy of the next node by referencing deep copy map
            deepCopyMap[curr]->next = deepCopyMap[curr->next];

            //do the same for random
            deepCopyMap[curr]->random = deepCopyMap[curr->random];

            curr = curr->next;
        }

        return deepCopyMap[head];
    }
};
