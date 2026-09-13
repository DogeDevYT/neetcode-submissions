"""
We can model this situation as a graph where each vertex is a word that is 1 character different from each connected
word. So an adjaceny list builder and then BFS should be the solution here. However, to pass leetcode/neetcode requirements, we need to have it so that we use wildcard substituion such that: hot -> (*ot, h*t, ho*) and dot -> (*ot, d*t, do*) so we need to create a hasmap basd on pattern: {*ot: [hot, dot, lot]}
"""
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #check if our end word is in our list (is this possible?)
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list) #when we append to a new key, default value will always be an empty list
        wordList.append(beginWord) #beginning word isn't in word list so we need to accoutn for that

        #build adjacency list
        for word in wordList:
            #iterate through every character and replace with wildcard
            for j in range(len(word)):
                #split word up to j exclusive, add j, then start again at j+1 inclusive
                pattern = word[:j] + "*" + word[j+1:]
                #add our current word to our pattern key
                nei[pattern].append(word)
        
        #when we do our bfs we need to use a set ot make sure we dont' visit same word twice
        visit = set([beginWord])
        #use a deque for bfs implentatioun
        q = deque([beginWord])
        res = 1

        while q:
            #go through every node in queue at each level
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                #go through all possibilities and add to queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neiword in nei[pattern]:
                        #make sure we dont accidently visit smae word twice
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            #increment result by 1 after going through entire layer
            res += 1
        #this means we haven't found anything in terms of a path so we should return 0
        return 0