class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine the 2 different lists into a single list of pairs [position, speed]
        pairs = []
        for position, speed in zip(position, speed):
            pairs.append([position, speed])
        
        #python doens't have native stack implementation so just use list instead
        stack = []

        #itearte through the sorted list of pairs in descending order
        for p, s in sorted(pairs)[::-1]:
            # get the time needed to get to target
            time = (target - p) / s
            #push the times to the stack
            stack.append(time)

            #if the new cars time is <= the time before it, it must catch up to the 2nd most newest car
            #on the stack -> merge and pop from stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() #pop newest car length i.e. merge it with slowest car
        
        #return length from stack
        return len(stack)