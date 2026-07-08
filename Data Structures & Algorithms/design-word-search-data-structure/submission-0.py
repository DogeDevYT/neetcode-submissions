"""
Ok this one seems like a pretty basic Trie implmentation where we just have to design a hashmap to store characters
except this time we have to recurse for all values for when we get a . symbol
"""

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    
    """Literally the exact same as the previous chud Trie"""
    def addWord(self, word: str) -> None:
        #base case: word empty, meaning end of word
        if not word:
            self.is_end = True
            return
        
        #get first character and recurse through children/add to children
        first = word[0]

        if first not in self.children:
            self.children[first] = WordDictionary()
        
        #recurse through to children by chopping off first part
        return self.children[first].addWord(word[1:])

    """
    This should be a same basic trie search as before, except this time every time we encounter a "." we just recurse
    through all children instead
    """
    def search(self, word: str) -> bool:
        #base case, word empty so we have to check if our is end varaible is set to true
        if not word:
            return self.is_end
        
        #get first character
        first = word[0]

        if first == ".":
            #I think we can get around this any match character by having a result variable thats a 
            #disjunctive normal form of everythig
            ret = False

            for child in self.children.keys():
                ret = ret or self.children[child].search(word[1:])

                if ret: #early return
                    return True
            
            return False
        else:
            #this is the typical case where we dont have to do that much differnt from everything else
            if first not in self.children:
                return False
            
            return self.children[first].search(word[1:])
