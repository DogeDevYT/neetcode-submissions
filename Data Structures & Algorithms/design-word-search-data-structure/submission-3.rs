/*
I'm rusting it im rusting it im rusting it so good mark
*/

use std::default::Default;

struct TrieNode 
{
    children: [Option<Box<TrieNode>>; 26],
    word: bool,
}

impl TrieNode 
{
    fn new() -> Self 
    {
        TrieNode 
        {
            children: Default::default(),
            word: false,
        }
    }
}

struct WordDictionary {
    root: TrieNode,
}

impl WordDictionary {
    pub fn new() -> Self {
        WordDictionary 
        {
            root: TrieNode::new(),
        }
    }

    pub fn add_word(&mut self, word: String) {
        let mut cur = &mut self.root;
        for c in word.bytes() 
        {
            let idx = (c - b'a') as usize;
            cur = cur.children[idx].get_or_insert_with(||
                Box::new(TrieNode::new())
            );
        }
        cur.word = true;
    }

    pub fn search(&self, word: String) -> bool {
        Self::dfs(word.as_bytes(), 0, &self.root)
    }

    fn dfs(word: &[u8], j: usize, root: &TrieNode) -> bool 
    {
        let mut cur = root;
        for i in j..word.len() 
        {
            let c = word[i];
            if c == b'.' 
            {
                for child in &cur.children 
                {
                    if let Some(node) = child 
                    {
                        if Self::dfs(word, i + 1, node) 
                        {
                            return true;
                        }
                    }
                }
                return false;
            } else 
            {
                let idx = (c - b'a') as usize;
                match &cur.children[idx] 
                {
                    None => return false,
                    Some(node) => cur = node,
                }
            }
        }
        cur.word
    }
}
