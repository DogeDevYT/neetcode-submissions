#include <unordered_map>
#include <string>

class PrefixTree {
private:
    std::unordered_map<char, PrefixTree*> children;
    bool is_end;
public:
    PrefixTree() {
        children = {};
        is_end = false;
    }
    
    /*
    we can recurseively search and add elements as follows:

    if we hit empty string, we can go ahead and set this as the end to true. Otherwise we recurse down 
    into next character and add any necessary prefix tree pointers
    */
    void insert(string word) {
        if (word.empty()) 
        {
            is_end = true;
            return;
        }

        char first = word[0];

        if (!children.contains(first)) 
        {
            children[first] = new PrefixTree();
        }

        children[first]->insert(word.substr(1));
    }
    
    /*
    We have 2 possible base cases here:

    1: empty word string: return if this is the end of a word
    2: first character in word doesn't exist in children, return false

    and then just recurse into child node by chopping off one charcter as needed
    */
    bool search(string word) {
        if (word.empty()) return is_end;

        char first = word[0];

        if (!children.contains(first)) return false;

        //recurse down
        PrefixTree* child = children[first];
        return child->search(word.substr(1));
    }
    
    /*
    We can implement a recursive serach algorithm with the following 2 base cases:

    1: empty string: return true becuase we've sucessfully validated prefix
    2: first character in prefix doesn't exist in children, return false

    otherwise we can just recurse with the same type of logic
    */
    bool startsWith(string prefix) {
        if (prefix.empty()) return true;

        char first = prefix[0];

        if (!children.contains(first)) return false;

        //recurse
        PrefixTree* child = children[first];
        return child->startsWith(prefix.substr(1));
    }
};
