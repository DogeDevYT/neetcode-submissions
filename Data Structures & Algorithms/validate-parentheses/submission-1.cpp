#include <stack>
#include <unordered_map>

class Solution {
public:
    bool isValid(string s) {
        //create stack to denote open elements
        std::stack<char> openStack;
        //create hashmap to store closing combinations
        // Map closing brackets to their corresponding opening brackets
        // This makes lookup much easier than mapping open to close
        std::unordered_map<char, char> closeToOpen = {
            {'}', '{'},
            {')', '('},
            {']', '['}
        };

        for (const char& character : s) {
            // If the character is a closing bracket (it's a key in our map)
            if (closeToOpen.count(character)) {
                // If stack is empty or the top doesn't match the required opening bracket
                if (openStack.empty() || openStack.top() != closeToOpen[character]) {
                    return false;
                }
                openStack.pop(); // Match found, remove from stack
            } else {
                // It's an opening bracket, push it
                openStack.push(character);
            }
        }

        //check if stack is empty
        return openStack.empty();
    }
};
