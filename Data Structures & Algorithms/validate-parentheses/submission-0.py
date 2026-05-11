class Solution:
    """
    Ok this one might genuinely be the easiest algorithm to check ever so lets just go over the high level

    - we use a stack to trackk opening brackets
    - we also have a dictionary to store opening to closing matches so we can check for things like (}

    and then we run through all charcters
    """
    def isValid(self, s: str) -> bool:
        #create stack
        stack = []

        #create my open to close hash map
        openToClose = {"{": "}", "(": ")", "[":"]"}

        #iterate over every character in s
        for char in s:
            #opening bracket
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            else:
                #check if we have closing bracket to begin with and if so, return false
                if len(stack) == 0 and char not in openToClose:
                    return False
                #closing 
                if char != openToClose[stack[len(stack)-1]]:
                    return False
                #pop
                stack.pop()
        
        #now all we have to do is check if stack is empty
        return len(stack) == 0