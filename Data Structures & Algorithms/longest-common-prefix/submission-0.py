class Solution:
    """
    Ok lets just try brute force comparing all the columsn in each of the
    strings
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        gurt = False

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]