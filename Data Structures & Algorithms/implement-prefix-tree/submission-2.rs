/*
Rust doesn't work quite the same as the other languages in that we need to define seperate wrapper
classes to get the same kind of logic as the other types

Fundementally, this works out to be the same however since all we're basically making a hashmap of children
for each trie node in our prefix tree so we can just use the same structure where our words are the path and each
node is a ch arcter basically
*/

use std::collections::HashMap;

struct TrieNode 
{
    children: HashMap<char, TrieNode>,
    end_of_word: bool,
}

impl TrieNode 
{
    fn new() -> Self 
    {
        Self 
        {
            children: HashMap::new(),
            end_of_word: false,
        }
    }
}

struct PrefixTree {
    root: TrieNode,
}

impl PrefixTree {
    pub fn new() -> Self {
        Self 
        {
            root: TrieNode::new()
        }
    }

    pub fn insert(&mut self, word: String) {
        let mut cur = &mut self.root;
        
        for c in word.chars() 
        {
            cur = cur.children.entry(c).or_insert_with(TrieNode::new);
        }

        cur.end_of_word = true;
    }

    pub fn search(&self, word: String) -> bool {
        let mut cur = &self.root;
        for c in word.chars() 
        {
            match cur.children.get(&c) 
            {
                Some(node) => cur = node,
                None => return false,
            }
        }
        cur.end_of_word
    }

    pub fn starts_with(&self, prefix: String) -> bool {
        let mut cur = &self.root;
        for c in prefix.chars() 
        {
            match cur.children.get(&c) 
            {
                Some(node) => cur = node,
                None => return false,
            }
        }
        true
    }
}
