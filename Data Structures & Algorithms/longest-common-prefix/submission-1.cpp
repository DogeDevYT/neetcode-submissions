class Solution {
public:
    /*
    ok this one shouldn't be too hard. all we need to do is vertically
    iterate over the columns in a string and return the first string
    at its length OR one where the current character doesn't match
    the current character of hte first string
    */
    string longestCommonPrefix(vector<string>& strs) {
        for (int i = 0; i < strs[0].length(); i++) 
        {
            for (string s : strs) 
            {
                if (i == s.length() || s[i] != strs[0][i]) return s.substr(0, i);
            }
        }
        //our entire first string is included so we return that
        return strs[0];
    }
};