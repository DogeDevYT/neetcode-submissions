from collections import deque

class Solution:
    """
    Yeah I'm ngl I might just have to try brute force at first and then
    ask an LLM for the optomization. 


    Yeah so I found out we can actually use a monotically decreasing queue.
    to find the first index that fits our maximum I think? I dont quite
    understand this but hopefully after implemenation I will. 
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() #stores indicies of numbers

        for i in range(len(nums)):
            #maintain monotonic property by removing numbers from back
            #becuase that means they wont be included in teh sliding window
            #maximum to begin with because we want the maximum of each
            #sliding window of size k
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            #append current element to end of queue
            q.append(i)

            #remove front index from queue since its constantly asking
            #from MAX from list
            if q[0] < i - k + 1:
                q.popleft()

            #when sliding window is built up, we can start adding 
            #to our outpuit
            if i >= k - 1:
                output.append(nums[q[0]])
        return output