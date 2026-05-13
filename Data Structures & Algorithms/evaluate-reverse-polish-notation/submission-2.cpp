#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // Use an int stack to avoid unnecessary string conversions
        std::stack<int> numbers;

        for (const string& token : tokens) {
            // Check if token is an operator
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                // 1. Get the top element (b)
                int b = numbers.top();
                numbers.pop();
                
                // 2. Get the next top element (a)
                int a = numbers.top();
                numbers.pop();

                // 3. Perform operation and push back
                if (token == "+") numbers.push(a + b);
                else if (token == "-") numbers.push(a - b);
                else if (token == "*") numbers.push(a * b);
                else if (token == "/") numbers.push(a / b);
            } else {
                // It's a number: convert once and push
                numbers.push(std::stoi(token));
            }
        }

        return numbers.top();
    }
};