"""
I think we can get around this problem by storing a hashmap of values from 2-9 with possible letters and using
that to string together a backtrack solution here on each digit.

eg. 2: [abc]

and we backtrack on weather or not we choose somethign and move to next digit
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        res = []

        curr = [] #maybe we can use "".join() on this to get an induvidual result

        def backtrack(curr_digits):
            #base case for curr_digits having nothing left
            if not curr_digits:
                res.append("".join(curr))
                return
            
            digit = int(curr_digits[0])

            for option in phone_map[digit]:
                #backtrack on each possible combination
                curr.append(option)
                backtrack(curr_digits[1:])
                curr.pop()
        backtrack(digits)

        return res
            

        