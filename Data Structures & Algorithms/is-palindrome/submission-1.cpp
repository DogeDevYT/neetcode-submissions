#include <cctype> //need for this for std::isalnum, std::tolower

class Solution {
public:
    /*
    yeah honestly this ones super easy just have 2 pointers and check if they converge
    */

    bool isPalindrome(string s) {
        //intialize left and right pointers
        int l = 0;
        int r = s.length() - 1;

        //iterate while the left and right pointers haven't crossed each other
        while (l <= r) 
        {
            char left = s[l];
            char right = s[r];

            //std::tolower returns int so we need to cast back to char
            left = static_cast<char>(std::tolower(left));
            right = static_cast<char>(std::tolower(right));
            if (l < r) 
            {
                if (!std::isalnum(left)) 
                {
                    l++;
                } else if (!std::isalnum(right)) 
                {
                    r--;
                } else if (left != right) 
                {
                    return false;
                } else 
                {
                    //charcters are equal so we just increment
                    l++;
                    r--;
                }
            } else 
            {
                //since we have same character, they're guaranteed to be equal
                break;
            }
        }

        //if we get here,  it means its guarnteed to be vlaid
        return true;
    }
};
