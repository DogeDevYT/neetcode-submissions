#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /*
        For this solution we will first be creating a frequency
        map using a hashtable (implemented as hashmap)

        and then sorting these into n buckets such that 
        we have the frequency of each denote the "number" of the bucket

        We can then iterate backwards to get the k most common elements
        */

        //create frequency map
        std::unordered_map<int, int> freq;

        //populate frequency map
        for (int num : nums) 
        {
            if (!freq.contains(num)) 
            {
                freq[num] = 1;
            } else 
            {
                freq[num]++;
            }
        }

        //Create n buckets denoting frequency
        std::vector<vector<int>> buckets(nums.size() + 1); 
        //+1 so we can use direct index for frequency number

        //populate our buckets with values
        for (auto const& [val, count] : freq) 
        {
            buckets[count].push_back(val);
        }

        //create our solution vector we're returning
        std::vector<int> solution;

        //iterate through buckets backwards to find k most common elements
        for(int i = buckets.size() - 1; i >= 0; i--) 
        {
            //iterate through each number in possible bucket
            for (auto const& be : buckets[i]) 
            {
                solution.push_back(be);

                if (solution.size() == k) return solution;
            }
        }

        //we'll never get here so its chill
        return solution;
    }
};
