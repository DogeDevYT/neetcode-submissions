def isPrefixAndSuffix(a, b):
    return b.startswith(a) and b.endswith(a)

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    pairs += 1
        return pairs