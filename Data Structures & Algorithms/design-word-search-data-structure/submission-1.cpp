/*
Allright lets get this cpp slop over with 

the only real difference from basic Trie implmentation is to just iterate through the wildcar match for search
*/

#include <unordered_map>
#include <string>

class WordDictionary {
private:
    bool end; 
    std::unordered_map<char, WordDictionary*> children;
public:
    WordDictionary() {
        end = false;
        children = {};
    }
    
    //LITERALLY the EXACT same as the basic trie implementation
    void addWord(string word) {
        if (word.empty()) 
        {
            end = true;
            return;
        }

        char first = word[0];

        if (!children.contains(first)) children[first] = new WordDictionary();

        children[first]->addWord(word.substr(1));
    }
    
    //slihgtly different since we have a wildcard implementation
    bool search(string word) {
        if (word.empty()) return end;

        char first = word[0];

        if (first == '.') 
        {
            bool ret = false;

            for (const auto& [child, child_node] : children) 
            {
                ret = ret || children[child]->search(word.substr(1));

                if (ret) return true;
            }

            return false;
        } else 
        {
            if (!children.contains(first)) return false;

            return children[first]->search(word.substr(1));
        }
    }
};
