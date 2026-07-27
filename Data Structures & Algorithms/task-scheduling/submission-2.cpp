/*
Ok I think this problem requires 3 data structures: max heap, queue, and frequency map.

Basically first we populate the frequency map with each task and its frequency. Then we populate a max_heap with
frequency (frequency, letter), and also a queue with (remaining time, letter). We have to run a while loop while
we have EITHER the max heap or queue with elements with the 2 possible cases:

1) max heap elements exist so we pop off the heap and append a pair of values of (n, letter) to queue
2) pop off queue and append to heap with format (current frequency, letter) for next iteration

all the while we keep track of time and return time at end.

But since this is cpp we implement the max heap with a priority queue
*/

#include <unordered_map>
#include <queue>

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        //initialize our priority queue (max heap) (frequency, letter)
        std::priority_queue<std::pair<int, char>> max_heap;
        //initialize our task queue (remaining cooldown, letter)
        std::queue<std::pair<int, char>> q;
        //initialize our frequency hashmap
        std::unordered_map<char, int> freq;

        //populate frequency hashmap
        for (char task : tasks) 
        {
            if (!freq.contains(task)) 
            {
                freq[task] = 1;
            } else 
            {
                freq[task] += 1;
            }
        }

        //build max heap
        for (const auto& [letter, letter_freq] : freq) 
        {
            max_heap.push({letter_freq, letter});
        }

        //variable to store elapsed time
        int time = 0;

        //iterate over scheduling until both the max heap and the task queue is empty
        while (!max_heap.empty() || !q.empty()) 
        {
            //case 1 - we pop something off heap
            if (!max_heap.empty()) 
            {
                std::pair<int, char> heap_item = max_heap.top();
                max_heap.pop();

                int freq_val = heap_item.first;
                char letter = heap_item.second;

                freq[letter] = freq_val - 1;

                if (freq[letter] > 0) 
                {
                    q.push({time + n, letter});
                }

                if (!q.empty()) 
                {
                    //check to see if anything in queue can be added
                    std::pair<int, char> q_item = q.front();

                    int timestamp = q_item.first;
                    int q_letter = q_item.second;

                    if (timestamp == time) 
                    {
                        max_heap.push({freq[q_letter], q_letter});
                        q.pop();
                    }
                }
                time++;
            } else 
            {
                //in this case we need to pop off the queue and append to the heap with (frequency, latter)
                //and advance time forward (q timestamp - current time) + 1

                std::pair<int, char> q_item = q.front();
                q.pop();

                int remaining_time = q_item.first;
                char letter = q_item.second;

                max_heap.push({freq[letter], letter});

                time += (remaining_time - time) + 1;
            }
        }
        return time;
    }
};
