/*
The naive O(n^3) solution just reverses every possible substring combination
but we can optomize this by trying to extend each possible substring palindrome at each index i such that we keep expanding while (l >= 0 and r < s.size() and s[l] == s[r])
*/
class Solution {
private:
    //extend outward from each start index pair
    //we can get even/odd pairs by starting at i, i+1
    //and i, i respectively
    int extend_count(string s, int l, int r) 
    {
        int count = 0;

        while (l >= 0 && r < s.size() && s[l] == s[r]) 
        {
            count++;
            l--;
            r++;
        }
        return count;
    }
public:
    int countSubstrings(string s) {
        int palindrome_count = 0;

        for (int i = 0; i < s.size(); i++) 
        {
            //odd palindromes
            palindrome_count += extend_count(s, i, i);
            //even palindromes
            palindrome_count += extend_count(s, i, i+1);
        }

        return palindrome_count;
    }
};
