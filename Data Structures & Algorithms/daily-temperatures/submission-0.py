class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        #create stack of length of input
        answer = [0] * n
        stack = [] # this stores indicies

        #iterate through temperatures from left to right
        for i, current_temp in enumerate(temperatures):
            #while staack is not empty and current temp is warmer
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        
        return answer