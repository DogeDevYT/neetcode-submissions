#include <string>
#include <vector>

class Solution {
private:
    std::string s;
    std::vector<int> memo;

    int dfs(int i) {
        // Successfully decoded the entire string
        if (i == s.size()) {
            return 1;
        }

        if (memo[i] != -1) {
            return memo[i];
        }

        // '0' cannot be decoded by itself
        if (s[i] == '0') {
            return memo[i] = 0;
        }

        // Decode one digit
        int total = dfs(i + 1);

        // Decode two digits if they form 10–26
        if (
            i + 1 < s.size() &&
            (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))
        ) {
            total += dfs(i + 2);
        }

        return memo[i] = total;
    }

public:
    int numDecodings(std::string input) {
        s = input;
        memo.assign(s.size(), -1);
        return dfs(0);
    }
};