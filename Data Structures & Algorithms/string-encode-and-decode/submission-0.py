class Solution:
    """
    For this problem I'm thinking we can add the length + delimiter
    to each string and then use that to encode/decode

    e.g.

    cat, dog, rat

    3#cat3#dog3#rat
    """

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            final += str(len(word))
            final += "#"
            final += word
        
        return final



    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0

        while index < len(s):
            delimiterIndex = s.find("#", index)
            
            # Grab the full number before the #
            length = int(s[index:delimiterIndex])
            
            # Update index to point to the start of the actual string
            index = delimiterIndex + 1
            
            # Extract the word and add to list
            # Note: Use s[start:end] syntax, not s[start, end]
            decoded.append(s[index : index + length])
            
            # Move index to the beginning of the next 'length'
            index += length
        
        return decoded
