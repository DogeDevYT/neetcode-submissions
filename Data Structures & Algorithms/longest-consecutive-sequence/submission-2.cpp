class Solution {
public:
    /*
        I'm ngl this one was actually deceptively difficult so what we have to do is convert
        everything to a set and then run a while loop to check for some element x such that

        x-1 exists in the set

        and we keep running that while loop until that isn't true anymore while incrementing our depth (max length)
        and we just highkey return the maximum of that

        edit:

        we can optomize this by chekcing
        x + 1 exists in the set 
        and only starting when our x - 1 eleemnt doesn't exist, that we we wont iterate over every elemenet
    */
    int longestConsecutive(vector<int>& nums) {
        //intialize our set using cpp's range feature
        std::unordered_set<int> numsSet(nums.begin(), nums.end());

        //keep max depth for refernce later
        int maxDepth = 0;
        //iterate through every number in our new set
        for (const auto& num : numsSet) 
        {
            if (!numsSet.contains(num - 1)) 
            {
                //now we start our iteration counting trick
                int currDepth = 1;
                int numCopy = num; //store a copy becuase we're iterating const auto&

                //iterate forwards
                //using pre increment so we can make sure its correct in timme for check
                while (numsSet.contains(++numCopy)) 
                {
                    currDepth++; //increment depth
                }

                //update max depth
                maxDepth = std::max(currDepth, maxDepth);
            }
        }
        return maxDepth;
    }
};
