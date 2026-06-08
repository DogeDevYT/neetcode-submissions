class Solution {
public:
    /*
    Honestly this problem just sucks all around theres no way I would
    be able to get this on an actual interview even with getting the hint
    to treat each node in teh array like a  linked list value

    that last part about using a second slow pointer to isolate the 
    entrance of the cycle, and thus finding our return value
    */
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;

        while (true) 
        {
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (nums[slow] == nums[fast]) break;
        }

        //now we can isolate entrance
        int slow2 = 0;

        while (true) 
        {
            slow2 = nums[slow2];
            slow = nums[slow];

            if (slow == slow2) return slow;
        }
    }
};
