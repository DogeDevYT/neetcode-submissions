/*
After figuring out the trick of using the XOR operator in sequence, this problem wasn't hard at all
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = nums[0];

        for (int i = 1; i < nums.size(); ++i) res = res ^ nums[i];

        return res;
    }
};
