/*
We can model this situation as a graph where each vertex is a wrod that is 1 character different from each connected
word. So an adjacency list builder and BFS should be the solution here. However, to pass time constraints, we need to 
do it so that we have wildcard substitution such that: hot -> (*ot, h*t, ho*) and dot -> (*ot, d*t, do*) so we need
to create hashmap based on pattern: {*ot: [hot, dot, lot]}
*/

#include <unordered_map>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <algorithm>

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        //check if end word is in our list (i.e. is this possible?)
        if (!ranges::contains(wordList, endWord)) return 0;

        unordered_map<string, vector<string>> nei;
        //beginning word isn't in word list so we need to accoutn for that
        wordList.emplace_back(beginWord);

        // 2. Build pattern graph using `j` index directly
        for (const string& word : wordList) {
            for (int j = 0; j < word.size(); j++) {
                string pattern = word.substr(0, j) + "*" + word.substr(j + 1);
                nei[pattern].emplace_back(word);
            }
        }

        //create a set of words we've visited
        set<string> visited = {beginWord};
        //use a queue for bfs initialization
        queue<string> q;
        q.push(beginWord);

        int res = 1;

        while (!q.empty()) 
        {
            size_t q_len = q.size();

            for (int i = 0; i < q_len; i++) 
            {
                string word = q.front();
                q.pop();

                //we found our count
                if (word == endWord) return res;

                for (int j = 0; j < word.size(); j++) 
                {
                    string pattern = word.substr(0, j) + "*" + word.substr(j + 1);
                    nei[pattern].emplace_back(word);

                    vector<string> hits = nei[pattern];

                    for (string neiword : hits) 
                    {
                        if (!visited.contains(neiword)) 
                        {
                            visited.insert(neiword);
                            q.push(neiword);
                        }
                    }
                }
            }

            //increment count
            res++;
        }
        //if we get here it means finding the word sequnce is impossible
        return 0;
    }
};
