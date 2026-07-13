"""
This one seems really similar to combination sum I, honestly I think the only difference is that we 
ALWAYS increment our index by one wheather we decide to keep an element/skip it

update: forgot to skip duplicate elements so we need to sort candidates and then skip duplicate elements in our indices
"""

class Solution:
    def backtrack(self, candidates, target, curr_combo, index, res):
        if target == 0:
            res.append(curr_combo.copy())
            return
        
        if index >= len(candidates) or target < 0: return

        #decision to include
        curr_combo.append(candidates[index])
        self.backtrack(candidates, target - candidates[index], curr_combo, index + 1, res)

        #decision to skip
        curr_combo.pop()

        #remember to skip duplicate elements
        while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
            index += 1
        self.backtrack(candidates, target, curr_combo, index + 1, res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr_combo = []

        candidates = sorted(candidates) #sort to put into increasing order

        self.backtrack(candidates, target, curr_combo, 0, res)

        return res