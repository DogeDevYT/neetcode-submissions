struct TrieNode {
    children: HashMap<char, TrieNode>,
    is_word: bool,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            is_word: false,
        }
    }

    fn add_word(&mut self, word: &str) {
        let mut cur = self;
        for c in word.chars() {
            cur = cur.children.entry(c).or_insert_with(TrieNode::new);
        }
        cur.is_word = true;
    }
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = TrieNode::new();
        for w in &words {
            root.add_word(w);
        }

        let rows = board.len();
        let cols = board[0].len();
        let mut res = HashSet::new();
        let mut visit = vec![vec![false; cols]; rows];

        for r in 0..rows {
            for c in 0..cols {
                Self::dfs(&board, r as i32, c as i32, &root,
                          &mut String::new(), &mut visit, &mut res);
            }
        }
        res.into_iter().collect()
    }

    fn dfs(
        board: &Vec<Vec<char>>, r: i32, c: i32, node: &TrieNode,
        word: &mut String, visit: &mut Vec<Vec<bool>>,
        res: &mut HashSet<String>,
    ) {
        let rows = board.len() as i32;
        let cols = board[0].len() as i32;
        if r < 0 || c < 0 || r >= rows || c >= cols {
            return;
        }
        let (ru, cu) = (r as usize, c as usize);
        if visit[ru][cu] { return; }
        let ch = board[ru][cu];
        let next = match node.children.get(&ch) {
            Some(n) => n,
            None => return,
        };

        visit[ru][cu] = true;
        word.push(ch);
        if next.is_word {
            res.insert(word.clone());
        }

        Self::dfs(board, r + 1, c, next, word, visit, res);
        Self::dfs(board, r - 1, c, next, word, visit, res);
        Self::dfs(board, r, c + 1, next, word, visit, res);
        Self::dfs(board, r, c - 1, next, word, visit, res);

        word.pop();
        visit[ru][cu] = false;
    }
}