class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) return "";

        unordered_map<char, int> countT;
        for (char c : t) {
            countT[c]++;
        }

        pair<int, int> res = {-1, -1};
        int resLen = INT_MAX;

        for (int i = 0; i < s.length(); i++) {
            unordered_map<char, int> countS;
            for (int j = i; j < s.length(); j++) {
                countS[s[j]]++;

                bool flag = true;
                for (auto &[c, cnt] : countT) {
                    if (countS[c] < cnt) {
                        flag = false;
                        break;
                    }
                }

                if (flag && (j - i + 1) < resLen) {
                    resLen = j - i + 1;
                    res = {i, j};
                }
            }
        }

        return resLen == INT_MAX ? "" : s.substr(res.first, resLen);
    }
};