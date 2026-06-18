/*
Ok for this problem I think we can solve this quite simply with a hashmap that references a 
pair (since we're using cpp)

and we can store the hashmap as <key, pair[value, timestamp]> and just run binary search
with the actual timestamp
*/

#include <unordered_map>
#include <utility>
#include <vector>

class TimeMap {
private: 
    std::unordered_map<std::string, std::vector<std::pair<string, int>>> hashmap;
public:

    TimeMap() {
        
    }
    
    //handle insertion with pairs
    void set(string key, string value, int timestamp) {
        if (hashmap.contains(key)) 
        {
            hashmap[key].push_back({value, timestamp});
        } else 
        {
            std::vector<std::pair<string, int>> arr = {{value, timestamp}};
            hashmap[key] = arr;
        }
    }
    
    string get(string key, int timestamp) {
        std::string ret = ""; //initilize return value

        if (hashmap.contains(key)) 
        {
            std::vector<std::pair<string, int>> arr = hashmap[key]; //get reference to vec

            //time to run our binary search
            int l = 0;
            int r = arr.size() - 1;

            while (l <= r) 
            {
                int mid = (l + r) / 2;

                /*
                This is going to run a bit differently: since we're trying to find timestamp_prev <= timstamp
                we basically increment our left bound over and over and DONT exit early
                */

                if (arr[mid].second <= timestamp) 
                {
                    ret = arr[mid].first;
                    l = mid + 1;
                } else 
                {
                    r = mid - 1;
                }
            }
        }
        return ret;
    }
};
