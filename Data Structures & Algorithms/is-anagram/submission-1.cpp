class Solution {
public:
    bool isAnagram(string s, string t) {
        //immeidate case exit
        if (s.length() != t.length()) return false;

        //create vector to store letters from a-z
        std::vector<int> seen(26);
        std::vector<int> seen2(26);

        //iterate through all characters in string s
        for (char curr : s) 
        {
            std::cout << curr << " " << curr - 97 << std::endl;
            //convert character to ascii index by subtracting 97
            int index = curr - 97; 
            seen[index]++; //increment seen
        }

        //repeat for other string
        //iterate through all characters in string s
        for (char curr : t) 
        {
            std::cout << curr << " " << curr - 97 << std::endl;
            //convert character to ascii index by subtracting 97
            int index = curr - 97; 
            seen2[index]++; //increment seen
        }

        return seen == seen2;
    }
};
