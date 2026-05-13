class Solution:
    """
    for my initial solution, this should just be:

    if we have operator, perform operation on last 2 numbers in stack
    otherwise, push current number to stack
    """
    def evalRPN(self, tokens: List[str]) -> int:
        #initalize stack
        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) + int(b))
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) - int(b))
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) / int(b))
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) * int(b))
            else:
                #straight number
                stack.append(token)

        return int(stack.pop())