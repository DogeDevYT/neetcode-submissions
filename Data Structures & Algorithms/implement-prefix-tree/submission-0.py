"""
Ok this problem doesn't seem too bad, the whole idea is we need to get a Trie here (prefix tree)
I think we can just store characters as hashmap for each node and iterate through each depth by switching to 
the branch and have each node contain a list of characters as a hashmap
"""
class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False #we use this to check if we've traced out a word at a specific node
        

    def insert(self, word: str) -> None:
        #ok, this is going to work in the opposite order

        #base case 1: we've placed all characters
        if not word:
            self.is_end = True
            return
        
        first_char = word[0]

        #if the word doesn't exist yet, we need to create a new node branch
        if first_char not in self.children:
            self.children[first_char] = PrefixTree() #create a new node for the occasion

        #recurse down with suffix after chopping off one character
        self.children[first_char].insert(word[1:])


    def search(self, word: str) -> bool:
        #base case 1: sucessfully traced whole word
        if not word:
            return self.is_end
        
        first_char = word[0]

        #base case 2: next charcter/node Doesn't exist
        if first_char not in self.children:
            return False
        
        #recurse down to keep going for actual word and slice off first character
        child_node = self.children[first_char]
        return child_node.search(word[1:]) 
        

    """
    I think we can solve this using simple recursion i.e. we check for the following 2 possibilities:

    1. prefix is empty, meaning base case, return true
    2. first_char doesn't exist in children, base case, return false

    otherwise just recurse into children for specific node and keep going
    """
    def startsWith(self, prefix: str) -> bool:
        if not prefix: 
            return True
        
        if prefix[0] not in self.children:
            return False
        
        child_node = self.children[prefix[0]]
        return child_node.startsWith(prefix[1:])
        