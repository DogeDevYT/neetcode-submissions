#include <unordered_map>

class ListNode 
{
public:
    ListNode* prev;
    ListNode* next;
    int key;
    int val;

    //got it to work since I used an initializer list

    ListNode() : prev(nullptr), next(nullptr), key(-1), val(-1) {}

    ListNode(int k, int v) : prev(nullptr), next(nullptr), key(k), val(v) {}
};

class LRUCache {
private:
    int cap;
    unordered_map<int, ListNode*> cache;
    ListNode* head;
    ListNode* tail;

    //helper methods to add/remove
    void remove(ListNode* node) 
    {
        ListNode* prev = node->prev;
        ListNode* nxt = node->next;
        prev->next = nxt;
        nxt->prev = prev;
    }

    void insert(ListNode* node) 
    {
        ListNode* prev = tail->prev;
        prev->next = node; 
        node->prev = prev;
        node->next = tail; //should point to tail!
        tail->prev = node;
    }
public:
    LRUCache(int capacity) {
        cap = capacity;
        cache.clear();
        head = new ListNode(0, 0);
        tail = new ListNode(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) != cache.end()) 
        {
            ListNode* node = cache[key];
            remove(node);
            insert(node);
            return node->val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) 
        {
            remove(cache[key]);
            cache.erase(key);
        }
        ListNode* newNode = new ListNode(key, value);
        cache[key] = newNode;
        insert(newNode);

        if (cache.size() > cap) 
        {
            ListNode* lru = head->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }
    }
};
