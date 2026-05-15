class Solution:
    """
    Ok, for this solution. it was super hard. I had to ask gemini for help making an algorithm and I'm
    going to go ahead and try implmenting what it says and seeing if I can come back and understand it better.

    I know we need to use a stack (by context of what section of NC 150 im in) as well as fixing heights
    somehow becuase fixing lengths and taking minimum height takes too long. 

    but beyond that idk
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        #initialize empty stack to store indicies
        stack = []
        max_area = 0
        
        #append a 0 to the end of heights array to ensure every bar gets popped
        heights.append(0)

        #iterate through every index 
        for i in range(len(heights)):
            current_height = heights[i]

            #while heights is not empty and current height < height of bar on top of stack
            while stack and current_height < heights[stack[-1]]:
                #pop top index from stack: this is the index of bar whose area we're going ot calc
                h_index = stack.pop()

                height = heights[h_index]

                """
                for width, we need to calculate the right/left boundries

                for right: we can simply use the index we just found to be smaller than the previous
                for left: either -1 if stack is empty OR new top index of stack
                """
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)
            #append current index to stack
            stack.append(i)
        return max_area