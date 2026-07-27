"""
Ok for this problem I think what they're trying to get at is to create a hashmap of all characters and their frequency
and put the frequncies into a max -heap so we can process the most common one first (remember to pop it off the 
max-heap).

We also keep a priority queue off to the side to store task cooldowns (i.e. how many cycles after A do we need to 
wait before running A again).

If max-heap is empty, we just advance our time forward (to match next availible task in queue). Otherwise, I think
we should process the most frequent task in heap, decrement its frequency, and if its still valid, add it back to
the queue with its next availible time. 

If the task at the front of the queue becomes availible, we pop it and reinsert it into the heap.
"""

from collections import deque

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #make a hashmap for task frequencies
        freq = {}

        #populate frequency hashmap
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        #initialize our queue
        #im guessing its going to be stored with (<cooldown>, <character>) tuples
        q = deque()

        #initialize our count of cycles variable
        time = 0

        #initialize max heap
        max_heap = []

        #populate our max heap with (<frequency>, <letter>)
        for letter, freq_val in freq.items():
            max_heap.append([-freq_val, letter]) #remember to negate for max heap on heapify
        
        heapq.heapify(max_heap)

        #now that we have our setup we can finally start our task scheduler
        while max_heap or q:

            if max_heap:
                freq_val, letter = heapq.heappop(max_heap)
                freq_val = -freq_val #account for negation

                freq_val -= 1 #we just used the scheduler to process this task
                freq[letter] = freq_val

                #add it back to the task processing queue if its valid
                if freq_val > 0:
                    q.append([n + time, letter])
                
                #check most recent element in queue
                #and if its cooldown is over, add to max heap
                if q and q[0][0] == time:
                    _, letter = q.popleft()
                    heapq.heappush(max_heap, [-freq[letter], letter])
                
                time += 1
            else:
                #we dont need to iterate over all the values in queue because we process tasks one at a time
                #therefore we can add them one at a time -> just pop head of queue and add
                remaining_time, letter = q.popleft()

                heapq.heappush(max_heap, (-freq[letter], letter))
                
                time += (remaining_time - time) + 1
        return time
                
                